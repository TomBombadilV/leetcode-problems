# Maximum Product Subarray
# Time: O(n) | Space: O(1)

from math import inf
from typing import List

def maxProduct(nums: List[int]) -> int:
    if not(nums):
        return 0
    max_prod = -inf
    # First pass to get "left" negative product
    curr_prod = 1
    for n in nums:
        curr_prod = curr_prod * n
        max_prod = max(max_prod, curr_prod)
        # If n is 0, reset product
        curr_prod = 1 if n == 0 else curr_prod
    # Second pass to get "right" negative product
    curr_prod = 1
    for n in reversed(nums):
        curr_prod = curr_prod * n
        max_prod = max(max_prod, curr_prod)
        # If n is 0, reset product
        curr_prod = 1 if n == 0 else curr_prod
    return max_prod
        
cases = [   [2, 3, -2, 4],
            [-2, 0, -1],
            [],
            [0],
            [1],
            [-1, 1, -1, 1, -1],
            [100, -2, 2, 3, -2, 4, -300],
            [-2],
            [0, 2],
            [3, -1, 4],
            [-1, 100, -2, 2, 3, -2, 4, -300],
        ]
sols = [6, 0, 0, 0, 1, 1, 14400, -2, 2, 4, 2880000]

for i, c in enumerate(cases):
    ans = maxProduct(c)
    if ans == sols[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(c, ans, sols[i]))