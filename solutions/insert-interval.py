# Insert Interval
# Look at all intervals that are overlapping. Condense by preserving 
# min start and max end.
# Time: O(n) | Space: O(1)

from test import test
from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
    if not(intervals):
        return [newInterval]

    i = 0

    # Move past all intervals that are smaller than new interval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        i += 1
   
    # If new interval is greater than all intervals
    if i == len(intervals):
        return intervals + [newInterval]

    # If new interval is smaller than current interval (no overlap)
    if intervals[i][0] > newInterval[1]:
        intervals.insert(i, newInterval)
        return intervals
    
    # Condense intervals overlapping with new interval
    # Preserve start
    start = min(intervals[i][0], newInterval[0])

    # Preserve end, remove overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        end = max(intervals[i][1], newInterval[1])
        del[intervals[i]]
    
    # Add new interval
    intervals.insert(i, [start, end])
    return intervals

# Driver Code
cases = [   ([], [1, 1], [[1, 1]]),  # No current intervals
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),  # Overlap in beginning
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([[1, 2], [3, 4]], [5, 6], [[1, 2], [3, 4], [5, 6]]),
            ([[5, 6]], [3, 4], [[3, 4], [5, 6]]),
            ([[1, 1]], [1, 2], [[1, 2]]),
            ([[1, 1]], [1, 1], [[1, 1]]),
            ([[1, 3], [6, 8]], [2, 9], [[1, 9]]),
            ([[3, 5], [12, 15]], [6, 6], [[3, 5], [6, 6], [12, 15]]) 
]
test(insert, cases)
