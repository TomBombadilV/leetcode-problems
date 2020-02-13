# Maximum Subarray
# Deeeeeeeee Peeeeeeeee
# Time: O(n) | Space: O(n)

from typing import List
from math import inf

def maxSubArray(nums: List[int]) -> int:
    if not(nums):
        return 0
    max_sum = [-inf] * len(nums)
    for i, n in enumerate(nums):
        max_sum[i] = max(n + max_sum[i-1], n)
    return max(max_sum)

test_cases = [  [-2, 1, -3, 4, -1, 2, 1, -5, 4],
                [],
                [1, 2, 3, 4],
                [-2, -3, 0],
                [-1]
            ]
expected_solutions = [6, 0, 10, 0, -1]

for i, case in enumerate(test_cases):
    ans = maxSubArray(case)
    if ans == expected_solutions[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(case, ans, expected_solutions[i]))