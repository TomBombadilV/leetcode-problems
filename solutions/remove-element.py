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
    length = len(nums)
    while i < len(nums):
        if nums[i] == val:
            nums[:] = nums[:i] + nums[i + 1:]
            length -= 1
        else:
            i += 1
    return length

# Method 2
def removeElement(nums: List[int], val: int) -> int:
    length = 0
    end = 0
    for n in nums:
        if not(n == val):
            nums[end] = n
            length += 1
    return length

# Driver code
nums = [3, 2, 2, 3]
print(removeElement(nums, 3))
print(nums)

