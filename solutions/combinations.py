# Combinations

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    if n == 0 or k == 0:
        return []
    return recurse([i+1 for i in range(n)], k, [[]])

def recurse(nums: List[int], k: int, res: List[List[int]]):
    # If k is longer than amount of nums, there are no possible solutions
    if k > len(nums):
        return []
    # If k is 0, don't add any more nums
    if k == 0:
        return res
    # For each num with k-1 nums after it, add to solutions and recurse, using 
    # all the nums following num
    sols = []
    for i in range(len(nums) - k + 1):
        new_res = []
        for r in res:
            new_res.append(r + [nums[i]])
            sols = sols + recurse(nums[i+1:], k-1, new_res)
    return sols

n, k = 5, 2
print(combine(n, k))