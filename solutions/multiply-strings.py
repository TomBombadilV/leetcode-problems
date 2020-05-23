# Multiply Strings
# Method 1:
# Longform multiplication
# 
# Method 2:
# Karatsuba method

def multiply(num1: str, num2: str) -> str:
    
    # Put larger number as multiplicand, smaller as multiplier
    n, m = max(num1, num2), min(num1, num2)
    # Keep track of order of current digit in multiplier
    res, outer_order = 0, 1

    # Iterate through digits in multiplier
    for c_i in reversed(num2):
        i = int(c_i)
        curr_res, carry, inner_order = 0, 0, 1

        # Iterate through digits in multiplicand
        for c_j in reversed(num1):
            j = int(c_j)
            curr_res += (i * j + carry) % 10 * inner_order
            carry = (i * j + carry) // 10
            inner_order *= 10

        # Add result
        curr_res += carry * inner_order
        res += curr_res * outer_order
        outer_order *= 10
  
    return str(res)

# Driver Code
multiply('12', '9')
multiply('123', '456')
