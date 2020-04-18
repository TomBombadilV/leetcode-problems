# Contiguous Array
# Where 0 => -1 and 1 => 1, continuously sum the numbers. If sum = 0, then an
# equal number of 0s and 1s exist in string. Additionally, if we find a sum that
# was reached before, then we know that the string between those two indices
# must also equal 0.

from typing import List

def findMaxLength(nums: List[int]) -> int:
    # Dictionary where key is total and value is first index of total
    dic = {}
    # Running sum
    total = 0
    # Length of longest valid subarray
    max_length = 0
    # Iterate through entire array
    for i, num in enumerate(nums):
        # Update sum
        total += -1 if num == 0 else 1
        # If total is 0, this is longest subarray thus far 
        if total == 0:
            max_length = i + 1
        # If we have encountered total before, get the distance between 
        # instances of total
        elif total in dic:
            max_length = max(max_length, i - dic[total])
        # If neither, add total to dictionary
        else:
            dic[total] = i
    return max_length

# Driver code
cases = [   [0, 1],
            [0, 1, 0],
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 0, 1]
]
for case in cases:
    print(findMaxLength(case))
