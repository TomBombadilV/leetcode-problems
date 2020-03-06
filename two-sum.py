# Two Sum
# Use dictionary to iterate through list and check if each number's 
# "complement" exists
# Time: O(n) | Space: O(n)

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numDic = {}
    for curr_index in range(len(nums)):
        curr_num = nums[curr_index]
        addend = target - curr_num
        if addend in numDic:
            return [curr_index, numDic[addend]]
        else:
            numDic[curr_num] = curr_index