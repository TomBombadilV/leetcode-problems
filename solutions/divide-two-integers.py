# Divide Two Integers
# Method 1:
# Use subtraction

from test import test

def divide(dividend: int, divisor: int) -> int:
    res = 0
    signed = (divisor < 0) ^ (dividend < 0)
    divisor, dividend = abs(divisor), abs(dividend)
    while dividend >= divisor:
        res += 1
        dividend -= divisor
    return -res if signed else res

cases = [(10, 3, 3), (7, -3, -2)]
test(divide, cases)
