# Permutation Sequence
# Time: O(n) | Space: O(n)

from math import factorial
from typing import List

def getPermutation(n: int, k: int) -> str:
    nums = [i + 1 for i in range(n)]
    res = ''
    k = k - 1
    fac = factorial(n)
    while nums:
        fac = fac // n
        i = k // fac
        res = res + str(nums[i])
        nums = nums[:i] + nums[i + 1:]
        k = k % fac
        n = n - 1
    return res

tests = [(3, 3, "213"), (4, 9, "2314"), (0, 0, ""), (3, 1, "123"), (3, 5, "312"), (3, 6, "321"), (4, 24, "4321"), (1, 1, "1"), (3, 2, "132")]
for t in tests:
    n, k, ans = t
    res = getPermutation(n, k)
    check = "{0} passed".format(t) if res == ans else "{0} failed with {1} expected {2}".format(n, res, ans)
    print(check)