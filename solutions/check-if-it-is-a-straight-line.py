# Check if it is a Straight Line

from math import inf
from test import test
from typing import List

def checkStraightLine(coordinates: List[List[int]]) -> bool:
    if len(coordinates) <= 2:
        return True

    # Calculate slope between first pair of points
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (x2 - x1) / (y2 - y1) if y1 != y2 else inf
   
    # Check each coordinate's slope (calculated against first point) 
    # with first slope
    for i in range(2, len(coordinates)):
        x2, y2 = coordinates[i]
        curr_slope = (x2 - x1) / (y2 - y1) if y1 != y2 else inf
        if not(curr_slope == slope):
            return False

    return True

def CheckStraightLine(coordinates: List[List[int]]) -> bool:
    (x1, y1), (x2, y2) = coordinates[:2]
    
    # For each coordinate, check that the slope that current point makes with
    # first and second points are the same. Use multiplication to avoid
    # division by 0
    for x, y in coordinates:
        if not((x2 - x1) * (y - y2) == (x - x1) * (y2 - y1)):
            return False
    return True

cases = [ ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
          ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False),
          ([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]], True)
]
test(checkStraightLine, cases)
