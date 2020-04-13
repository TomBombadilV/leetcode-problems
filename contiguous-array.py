# Contiguous Array
# Where 0 => -1 and 1 => 1, continuously sum the numbers. If sum = 0, then an
# equal number of 0s and 1s exist in string. Additionally, if we find a sum that
# was reached before, then we know that the string between those two indices
# must also equal 0.

from math import inf
from typing import List

def findMaxLength(nums: List[int]) -> int:
    dic = {}
    total = 0
    max_length = 0
    for i, num in enumerate(nums):
        total += -1 if num == 0 else 1
        if total == 0:
            max_length = max(max_length, i + 1)
        elif total in dic:
            max_length = max(max_length, i - dic[total])
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
    print("NEW CASE ---------")
    print(findMaxLength(case))
