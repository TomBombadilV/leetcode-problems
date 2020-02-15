# Maximum Product Subarray

from math import inf
from typing import List

def maxProduct(nums: List[int]) -> int:
    sol = -inf
    curr_product = 1
    neg_indices = []
    for n in nums:
            if n == 0:
                curr_product = 1
            else:
                curr_product = curr_product * n
            sol = max(curr_product, sol)
            
    return sol
        
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