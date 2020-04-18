# 3Sum Closest
# Modified version of 3Sum. Use 3 pointers, with the first pointer iterating 
# through the list, and the other two pointers starting at the beginning and 
# end of the remaining part of the list, incrementing or decrementing according
# to the current position relative to the target.
# Time: O(n) | Space: O(1)

from math import inf
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    # Sort them so we can choose how to move our pointers
    nums = sorted(nums)
    # Keep track of the closest number
    closest = inf
    # Iterate first pointer through entire list
    for i in range(len(nums) - 2):
        # Small optimization to avoid checking duplicates
        if i > 0 and nums[i] == nums[i-1]:
            pass
        else:
            # Check window to the right of i, starting at beginning and end
            j, k = i + 1, len(nums) - 1 
            # Make sure j and k don't cross each other
            while j < k:
                # Get current sum
                curr_sum = nums[i] + nums[j] + nums[k]
                # See how far it is from target
                diff = curr_sum - target
                # See if it is closer than the current closest
                closest = curr_sum if abs(diff) < abs(closest - target) else closest
                # If current sum is to the right of the target, move the large
                # pointer to a smaller number
                if diff > 0:
                    k -= 1
                # If current sum is smaller than the target, move the small
                # pointer to a larger number
                elif diff < 0:
                    j += 1
                # If current sum is same as target, return
                else:
                    return curr_sum
    return closest

# Driver code
nums = [-100, -50, 0, 50, 100]
target = 1
print(threeSumClosest(nums, target))
