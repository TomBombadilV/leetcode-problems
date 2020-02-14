# LeetCode Two_Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target: int):
    numDic = {}
    for curr_index in range(len(nums)):
        curr_num = nums[curr_index]
        addend = target - curr_num
        if addend in numDic:
            return [numDic[addend], curr_index]
        else:
            numDic[curr_num] = curr_index

nums = [0, 10, 6, 6, 3]
target = 12
print(twoSum(nums, target))