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

def subarraySum(nums: List[int], k: int) -> int:
    i, j = 0, 0
    count = 0
    curr_sum = nums[i]
    while j < len(nums) and i <= j:
        if curr_sum < k:
            j += 1
            curr_sum += nums[j] if j < len(nums) else 0
        elif curr_sum > k:
            curr_sum -= nums[i]
            i += 1
        else:
            count += 1
            curr_sum -= nums[i]
            i += 1
    return count

def subarraySum(nums: List[int], k: int) -> int:
    count, running_sum = 0, 0
    sums = defaultdict(int)
    sums[0] = 1
    for n in nums:
        running_sum += n
        diff = running_sum - k
        count += sums[diff]
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
