# Sort Colors
# Since we know there are only three possible integers, we can place instances 
# of 2 at the end of the array, instances of 0 at the beginning, and instances 
# of 1 in the middle (at the end of where the zeroes are. We'll keep track of 
# the index)
# Time: O(n) | Space: O(1)

from typing import List

def sortColors(nums: List[int]) -> None:
    curr = 0
    # The index where the twos are. Also where you can stop sorting
    twos_index = len(nums)
    while curr < twos_index:
        if nums[curr] == 0:
            # Move it to beginning of array
            nums.insert(0, nums.pop(curr))
            curr += 1
        elif nums[curr] == 1:
            # Leave where it is, increment one's index
            curr += 1 
        # num is 2
        else:
            # Move it to the end of the array
            nums.append(nums.pop(curr))
            twos_index -=1 

cases = [   [2, 0, 2, 1, 1, 0],
            [],
            [0],
            [1],
            [2],
            [2,0]
        ]
for case in cases:
    print(case, end=" => ")
    sortColors(case)
    print(case)