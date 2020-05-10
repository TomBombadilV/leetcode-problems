# Find the Town Judge
# Keep track of how many people trust each person, as well as whether each person
# trusts anyone or not.
# Time: O(trust + N) | Space: O(N)

from test import test
from typing import List

def findJudge(N: int, trust: List[List[int]]) -> int:

    # Which people trust each person
    trusted_by = [[] for _ in range(N)]
    # Whether each person trusts anyone
    potential_judges = [True] * N
    
    # Go through all relationships to update arrays
    for truster, trustee in trust:
        # Truster can't be judge
        potential_judges[truster - 1] = False
        # Add truster to trustee's list
        trusted_by[trustee - 1].append(truster - 1)

    # Check each person who doesn't trust anyone to see if everyone else trusts them
    for judge, canJudge in enumerate(potential_judges):
        if canJudge and len(trusted_by[judge]) == N - 1:
            return judge + 1

    # If no judge found, return -1
    return -1 

# Driver Code
cases = [(2, [[1, 2]], 2),
         (3, [[1, 3], [2, 3]], 3),
         (3, [[1, 3], [2, 3], [3, 1]], -1),
         (3, [[1, 2], [2, 3]], -1),
         (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3)
]
test(findJudge, cases)
