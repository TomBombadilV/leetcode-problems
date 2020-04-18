# Remove Duplicates from Sorted Array
# Method 1: 
# Alter the input array using string manipulation, cutting out the repeated number
# Method 2: 
# Use a pointer to mark where the valid string currently ends. If a non-repeated
# number is encountered, place it at the end pointer.
# Time: O(n) | Space: O(1)

from typing import List

# Method 1
def removeDuplicates_1(nums: List[int]) -> int:
    # Skip index 0 since it can't be a duplicate
    i = 1
    # Keep track of valid length. Decreases every time duplicate is encountered 
    length = len(nums)
    while i < len(nums):
        # If num is same as previous num, remove it
        if nums[i] == nums[i - 1]:
            # nums = ... would cause a to point to a new list. nums[:] = will 
            # use slice assignment to modify the original list
            nums[:] = nums[:i] + nums[i + 1:]
            length -= 1
        # Don't iterate if you deleted something or else you'll skip the next one
        else:
            i += 1 
    return length

# Method 2
def removeDuplicates(nums: List[int]) -> int:
    # No empty list plz
    if not(nums): return 
    # Pointer where end of valid list is
    end = 1
    # Skip index 0 since it can't be a duplicate'
    for i in range(1, len(nums)):   
        # If not a duplicate, add to end of valid list
        if not(nums[i] == nums[i - 1]):
            nums[end] = nums[i]
            end += 1
    return end

# Driver Code
nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates_1(nums))
print(nums)
