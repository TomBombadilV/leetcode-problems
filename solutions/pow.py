# Recursively implement pow(x, n)

# Times out :(
def myPow(x: float, n: int) -> float:
    # If n is negative
    neg = True if n < 0 else False
    n = abs(n)
    
    def recurse(x: float, n: int) -> float:
        if n == 0:
            return 1
        return x * myPow(x, n - 1)
    
    res = recurse(x, n)
    return 1/res if neg else res

# Calculate half of the exponent, then multiply both halves together to avoid
# making the same computation multiple times. For example, n^10 = n^5 * n^5
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    # If n is negative, 1/x
    if n < 0:
        x = 1/x
        n = abs(n)
    # If n is odd, then we need to multiply the result by x one extra time
    odd = x if n % 2 == 1 else 1
    # Get half of the exponent
    res = myPow(x, n//2)
    return res * res * odd

# Driver code
print(myPow(2.0000, 10))
