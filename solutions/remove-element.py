# Remove Element
# Method 1:
# Modify the array using slice assignment whenever target is encountered
# Method 2:
# Use a pointer to keep track of end of valid array. Whenever target is 
# encountered, skip it and move all valid numbers to valid array
# Time: O(n) | Space: O(1)

from typing import List

# Method 1
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    # Length decrements whenever target is found
    length = len(nums)
    while i < len(nums):
        # If num equals target, use slice assignment to cut it out
        if nums[i] == val:
            nums[:] = nums[:i] + nums[i + 1:]
            length -= 1
        # Only increment if a number has not been cut out
        else:
            i += 1
    return length

# Method 2
def removeElement(nums: List[int], val: int) -> int:
    # Keep track of length and end index of valid string
    length, end = 0, 0
    for n in nums:
        # If number is not target, add to valid string
        if not(n == val):
            nums[end] = n
            end += 1
            length += 1
    return length

# Driver code
nums = [3, 2, 2, 3]
nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(removeElement(nums, 2))
print(nums)

