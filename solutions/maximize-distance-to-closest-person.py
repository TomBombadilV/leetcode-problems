# Maximize Distance to Closest Person

from test import test
from typing import List

def maxDistToClosest(seats: List[int]) -> int:
    """ Calculate seat farthest from other people.

        Two-pass method - calculates distance looking to the right, 
        distance looking to the left, then finds the closest person 
        based on those.
    """
    dist, max_dist = -1, 0
    to_right = [-1 for _ in range(len(seats))]

    # Calculate distance from each seat looking to the right
    for i, seat in reversed(list(enumerate(seats))):
        dist = 0 if seat == 1 else dist + 1 if dist > -1 else -1
        to_right[i] = dist
   
    # Reset current distance
    dist = -1

    # Calculate distance from each seat looking to the left
    for i, seat in enumerate(seats):
        dist = 0 if seat == 1 else dist + 1 if dist > -1 else -1
        
        # Calculate current distance to nearest person
        curr_max_dist = min(dist, to_right[i]) if dist > -1 and to_right[i] > -1 else\
            dist if dist > -1 else to_right[i]
        
        # Upd
        if curr_max_dist > max_dist:
            max_dist = curr_max_dist

    return max_dist
   
# Driver Code
cases = [
    ([1,0,0,0,1,0,1], 2),
    ([1,0,0,0], 3),
    ([0,1], 1)
]
#test(maxDistToClosest, [cases[0]])
test(maxDistToClosest, cases)
