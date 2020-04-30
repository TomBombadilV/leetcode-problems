# Jump Game
# Keep track of the limit of "jumpable" indices. Iterate through them, updating
# the limit each time. Once all jumpable indices have been visited, check if 
# the last index is within the range of "jumpable" indices.
# Time: O(n) | Space: O(1)

from typing import List

def canJump(nums: List[int]) -> bool:
    i, j = 0, 0
    # Search all jumpable indices
    while i <= j and i < len(nums):
        # Update limit of indices
        j = max(j, i + nums[i])
        i += 1
    # Check if last index is within jumpable limit
    return j >= len(nums) - 1
    

# Driver Code
cases = [([2, 3, 1, 1, 4], True),
         ([3, 2, 1, 0, 4], False),
         ([], True),
         ([1, 2, 3, 4], True),
         ([1, 1, 1, 1], True),
         ([1, 0, 1], False),
         ([3, 2, 1, 5, 0, 0, 1], True)
]
for case in cases:
    nums, expected = case
    res = canJump(nums)
    print("Passed" if res == expected else "Failed {0} with {1}".format(nums, res))
