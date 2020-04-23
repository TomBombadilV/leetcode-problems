# Bitwise AND Of Numbers Range
# Method 1
# In range (m, n), AND will only be nonzero if m and n have the same leading bit
# ex: 1xxxx and 1xxxx. This is because every time a jump from 2^n to 2^(n+1) 
# occurs, all bits are zeroed out except for the new leading bit. Apply this by 
# saving the shared bit and then looking at the rest of the bits.
# Time: O(n) | Space: O(1)

# Method 2
# Shave off the bits that are not the same from left to right, keeping track of 
# how many have been shaved off
# Time: O(n) | Space: O(1)

from math import log

# Method 1
def rangeBitwiseAnd(m: int, n: int) -> int:
    # Number representing m -> n AND
    range_and = 0
    while m and n:
        # Calculate the leftmost 1 bit
        order_m, order_n = int(log(m, 2)), int(log(n, 2))
        # If they aren't the same, there won't be any more shared bits
        if not(order_m == order_n):
            return range_and
        # If they are the same, add to AND number
        else:
            range_and += 2**order_m
        # Remove shared bit and check rest of the number
        m -= 2 ** order_m
        n -= 2 ** order_m
    return range_and

# Method 2
def rangeBitwiseAnd(m: int, n: int) -> int:
    # How many bits have been shaved off the end
    shaved = 0
    # As long as numbers aren't equal, shave 1 bit off
    while not(m == n):
        m >>= 1
        n >>= 1
        # Increment number of shaved bits
        shaved += 1
    # m and n are equal, so shared AND is either number shifted by number of
    # shaved bits
    return m << shaved

# Driver code
cases = [(5, 7), (1, 1), (1, 0), (3, 8)]
for case in cases:
    m, n = case
    print(rangeBitwiseAnd(m, n))
