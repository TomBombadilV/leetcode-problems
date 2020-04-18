# Single Number
# Method One: Use counter dict. After first pass, see which one only has 1 count. 
# Method Two: XOR all the numbers with 0. The duplicates will cancel each other out

from typing import List

def singleNumber(nums: List[int]) -> int:
    xor = 0
    for n in nums:
        xor = xor ^ n
    return xor

test_cases = [  [2, 2, 1],
                [4, 1, 2, 1, 2]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, singleNumber(case)))