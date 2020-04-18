# Jump Game II
# Time: O(n) | Space: O(n)

from typing import List

def jump(nums: List[int]) -> int:
    res = [0] * len(nums)
    farthest_i = 0
    for i, n in enumerate(nums):
        for j in range(farthest_i + 1, min(i + n + 1, len(nums))):
            res[j] = res[i] + 1
        farthest_i = max(farthest_i, i + n)
    return res[-1]

cases = [   [2, 3, 1, 1, 4], 
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0],
            [100, 0],
            [1, 2, 3],
            [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
]
for case in cases:
    print(case, jump(case))