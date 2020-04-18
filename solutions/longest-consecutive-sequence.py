# Longest Consecutive Sequence
# 

from collections import defaultdict
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    dic =  defaultdict()
    for n in nums:
        

cases = [[100, 4, 200, 1, 3, 2], [4, 4, 4, 4], [], [1, 3, 5, 7, 9]]
sols = [4, 1, 0, 0]
for i, c in enumerate(cases):
    ans = longestConsecutive(c)
    if ans == sols[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(c, ans, sols[i]))