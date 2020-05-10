# Valid Perfect Square

from collections import defaultdict
from test import test

# Times out
def isPerfectSquare(num: int) -> bool:
    factors = defaultdict(int)
    i = 2
    while num > 1:
        while num % i == 0:
            print("Factor ", i)
            factors[i] += 1
            num //= i
        i += 1
    for key in factors:
        if factors[key] % 2 == 1:
            return False
    return True

def isPerfectSquare(num: int) -> bool:
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 < num:
            left = mid + 1
        elif mid ** 2 > num:
            right = mid - 1
        else:
            return True
    return False

# Driver Code
cases = [(49, True), (14, False), (1, True), (20, False), (2147483647, False)]
test(isPerfectSquare, cases)
