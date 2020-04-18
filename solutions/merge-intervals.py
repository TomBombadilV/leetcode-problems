# Merge Intervals
# Sort the intervals, then check the beginning and end of each consecutive set 
# to see if they should be merged
# Time: O(nlogn) | Space: O(1)

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x:(x[0],-x[1]))
    i = 0
    while i < len(intervals) - 1:
        left, right = intervals[i], intervals[i+1]
        # If intervals overlap
        if right[0] <= left[1]:
            # And second interval is eclipsed by first
            if right[1] <= left[1]:
                intervals = intervals[:i+1] + intervals[i+2:]
            # And second interval extends past first
            else:
                intervals = intervals[:i] + [[left[0], right[1]]] + intervals[i+2:]
        # If intervals don't overlap
        else:
            i+=1
    return intervals
        

test_cases = [  [[1, 3], [2, 6], [8, 10], [15, 18]],
                [[1, 4], [4, 5]],
                [[1, 10], [1, 5], [2, 3], [2, 5], [7, 8]],
                []
            ]

for case in test_cases:
    print("{0} => {1}".format(case, merge(case)))