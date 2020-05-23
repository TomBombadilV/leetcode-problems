# Multiply Strings
# Method 1:
# Longform multiplication
# 
# Method 2:
# Karatsuba method

def multiply(num1: str, num2: str) -> str:
    """
    Method 1
    """

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

def multiply_k(num1: str, num2: str) -> str:
    """
    Method 2
    """
    if int(num1) == 0 or int(num2) == 0:
        return '0'

    if max(len(num1), len(num2)) == 1:
        return str(int(num1) * int(num2))

    split = -(-max(len(num1), len(num2)) // 2)

    num1 = num1.rjust(split * 2, '0')
    num2 = num2.rjust(split * 2, '0')

    a, b = num1[:split], num1[split:]
    c, d = num2[:split], num2[split:]

    ac = int(multiply_k(a, c))
    bd = int(multiply_k(b, d))

    abcd = int(multiply_k(str(int(a) + int(b)), str(int(c) + int(d))))
    abcd = abcd - bd - ac 

    return str((ac * (10 ** (split * 2))) + (abcd * 10 ** split) + bd)

# Driver Code
print(multiply_k('12', '9'))
print(multiply_k('123', '456'))
