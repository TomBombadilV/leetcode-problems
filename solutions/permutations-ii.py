# Permutations II
# Same deal except with duplicates in array
# Time: O(n!) | Space: O(n!)

from collections import Counter
from typing import Dict, List, Set

def permuteUnique(nums: List[int]) -> List[List[int]]:
    if not(nums):
        return []
    #return recurse_counter(Counter(nums), [[]])
    return [list(r) for r in recurse_set(nums, {()})]

# Counter Method
def recurse_counter(nums: Dict[int, int], res: List[List[int]]) -> List[List[int]]:
    if len(nums) == 0:
        return res
    final_res = []
    for n in list(nums.keys()):
        new_res = [r + [n] for r in res]
        new_nums = {k:v for k, v in nums.items()}
        new_nums[n] -=1
        if new_nums[n] < 1:
            del new_nums[n]
        final_res = final_res + recurse_counter(new_nums, new_res)
    return final_res

# Set Method
def recurse_set(nums: List[int], res: Set[List[int]]) -> Set[List[int]]:
    if len(nums) == 0:
        return res
    final_res = set()
    for i, n in enumerate(nums):
        new_res = {r + (n,) for r in res}
        final_res = final_res.union(recurse_set(nums[:i] + nums[i + 1:], new_res))
    return final_res

print(permuteUnique([1, 1, 2]))