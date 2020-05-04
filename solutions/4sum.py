# 4Sum
# Use dictionary to save sums of all possible pairs. Then go through each sum, checking
# if its complement exists in the dictionary and making sure indices are not repeated. 
# Time: O(n^2) | Space: O(n(n-2)/2)

from collections import defaultdict
from test import test
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    res = set()

    # Create dictionary of all pair sums and their indices
    dic = defaultdict(list)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum_ij = nums[i] + nums[j]
            dic[sum_ij].append((i, j))
    
    # Check if each key's complement exists in dictionary
    for key in dic:
        if target - key in dic:
            # If complement exists, iterate through each list
            l1, l2 = dic[key], dic[target - key]
            for i, j in l1:
                for k, l in l2:
                    # Make sure no repeated indices
                    if not i == k and not i == l and not j == k and not j == l:
                        # Sort to make sure set removes repeated groups
                        curr = sorted([nums[i], nums[j], nums[k], nums[l]])
                        res.add(tuple(curr))
    return list(res)

# Driver Code
cases = [ ([1, 0, -1, 0, -2, 2], 0, []),
          ([0, 0, 0, 0], 0, [[0, 0, 0, 0]])
]
test(fourSum, cases)
