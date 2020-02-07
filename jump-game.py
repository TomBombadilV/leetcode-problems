# Jump Game
# Select the number that gets you the farthest, then search in its range for 
# the next number that gets you the farthest. Ignore the ones that were already 
# checked in the previous range
# Time: O(n) | Space: O(1)

from typing import List

def canJump(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    curr = 0
    while curr < len(nums):
        if nums[curr] == 0:
            return False
        if nums[curr]+curr >= len(nums)-1:
            return True
        max_jump = (curr, -1)
        for i in range(nums[curr]):
            temp_jump_index = curr+i+1
            if temp_jump_index >= len(nums):
                return True
            temp_jump = nums[temp_jump_index] + temp_jump_index
            max_jump = (temp_jump_index, temp_jump) if temp_jump > max_jump[1] else max_jump
        curr = max_jump[0]
    

test_cases = [[2, 3, 1, 1, 4], [
                3, 2, 1, 0, 4], 
                [], 
                [0], 
                [0, 1], 
                [2, 0, 0],
                [5,9,3,2,1,0,2,3,3,1,0,0]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, canJump(case)))