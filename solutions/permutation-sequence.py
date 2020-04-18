# Permutation Sequence
# Do maffs based on pattern of permutation (each number is repeated (n-1)! 
# times at each level)
# Time: O(n) | Space: O(n)

from math import factorial
from typing import List

def getPermutation(n: int, k: int) -> str:
    # Array of possible nums
    nums = [i + 1 for i in range(n)]
    res = ''
    # Go to 0-based indexing
    k = k - 1
    fac = factorial(n)
    while nums:
        # (n - 1)!
        fac = fac // n
        # Get correct index in possible nums
        i = k // fac
        # Add to result
        res = res + str(nums[i])
        # Remove used num from nums
        nums = nums[:i] + nums[i + 1:]
        # Narrow scope of k
        k = k % fac
        # Length decreases
        n = n - 1
    return res

tests = [(3, 3, "213"), (4, 9, "2314"), (0, 0, ""), (3, 1, "123"), (3, 5, "312"), (3, 6, "321"), (4, 24, "4321"), (1, 1, "1"), (3, 2, "132")]
for t in tests:
    n, k, ans = t
    res = getPermutation(n, k)
    check = "{0} passed".format(t) if res == ans else "{0} failed with {1} expected {2}".format(n, res, ans)
    print(check)