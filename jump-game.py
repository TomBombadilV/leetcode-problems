# Jump Game
# Select the number that gets you the farthest, then search in its range for 
# the next number that gets you the farthest. Ignore the ones that were already 
# checked in the previous range
# Time: O(n) | Space: O(1)

from typing import List

def canJump(nums: List[int]) -> bool:
    # Any array size 0 or 1 can be ignored
    if len(nums) < 2:
        return True
    # Keep track of the farthest index you can reach so far
    farthest_index = 0
    for i, num in enumerate(nums):
        # If you can't reach this index from previous indices, then break
        if i > farthest_index:
            return False
        # Update farthest index
        farthest_index = max(farthest_index, i + num)
        # If you can already reach the end, then break
        if farthest_index >= len(nums) - 1:
            return True
    return True

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