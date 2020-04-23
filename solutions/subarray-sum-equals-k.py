# Subarray Sum Equals K
# Method 1:
# Use sliding window DP method. Start at beginning with two pointers. If 
# current sum is less than target, move right pointer. If current sum is more
# than target, move left pointer. Keep track of how many times target is hit
# Time: O(n) | Space: O(1)
# 
# Method 2:
# Use running sum method. Keep adding each successive number to the running
# sum and save it to dictionary. If sum - target exists in dictionary, then 
# a subarray exists from (sum - target) to sum.
# Time: O(n) | Space: O(n)

from collections import defaultdict
from typing import List

# Method 1
def subarraySum(nums: List[int], k: int) -> int:
    # Pointers to keep track of current window
    i, j = 0, 0
    # Number of subarrays that sum to k
    count = 0
    # Running sum
    curr_sum = nums[i]
    # While window is valid (doesn't run past end of array and pointers don't 
    # cross)
    while j < len(nums) and i <= j:
        # Sum is too small, make window larger to the right
        if curr_sum < k:
            j += 1
            # Update curr sum to include new number, unless window now extends
            # past end of array
            curr_sum += nums[j] if j < len(nums) else 0
        # Sum is too big, make window smaller from the left
        elif curr_sum > k:
            curr_sum -= nums[i]
            i += 1
        # Sum is juuuuust right. Add to count, make window smaller from the left
        # so we can explore for more subarrays
        else:
            count += 1
            curr_sum -= nums[i]
            i += 1
    return count

# Method 2
def subarraySum(nums: List[int], k: int) -> int:
    # Number of subarrays that sum to k, running sum
    count, running_sum = 0, 0
    # Dictionary of all running sums
    sums = defaultdict(int)
    # Add 0 to running sum so we can compare to "beginning"
    sums[0] = 1
    # Iterate through list
    for n in nums:
        # Update running sum to include new number
        running_sum += n
        # Calculate what previous running sum would have to exist in order for
        # current index to sum to k
        diff = running_sum - k
        # If that diff value was encountered before, we've found a k subarray
        count += sums[diff]
        # Add new running sum to dictionary
        sums[running_sum] += 1 
    return count

# Driver code
cases = [   ([1, 1, 1], 2),
            ([10, 8, 2, 1, 3, 10, 3, 1, 5, 1], 10),
            ([1], 1),
            ([1], 2),
            ([5, 5, 5], 0),
            ([-1, -1, 1], 0),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
]
for case in cases:
    l, k = case
    print(subarraySum(l, k))
