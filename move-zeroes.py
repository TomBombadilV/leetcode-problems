# Move Zeroes

from typing import List

def moveZeroes(nums: List[int]) -> None:
    j = 0
    for n in nums:
        if n != 0:
            nums[j] = n
            j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)