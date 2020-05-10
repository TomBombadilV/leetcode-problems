# Find the Town Judge
# Method 1:
# Keep track of how many people trust each person, as well as whether each person
# trusts anyone or not.
# Time: O(trust + N) | Space: O(N)
#
# Method 2:
# Keep track of count of how many people trust each person. If person trusts 
# someone else, decrease their count. A judge will have an exact count of N - 1
# Time: O(trust + N) | Space: O(N)

from test import test
from typing import List

def findJudge(N: int, trust: List[List[int]]) -> int:
    """
    Method 1
    """
    # Which people trust each person
    trusted_by = [[] for _ in range(N + 1)]
    # Whether each person trusts anyone
    potential_judges = [True] * (N + 1)
    
    # Go through all relationships to update arrays
    for truster, trustee in trust:
        # Truster can't be judge
        potential_judges[truster] = False
        # Add truster to trustee's list
        trusted_by[trustee].append(truster)

    # Check each person who doesn't trust anyone to see if everyone trusts them
    for judge, canJudge in enumerate(potential_judges):
        if canJudge and len(trusted_by[judge]) == N - 1:
            return judge

    # If no judge found, return -1
    return -1 

def findJudge(N: int, trust: List[List[int]]) -> int:
    """
    Method 2
    """
    # How many people trust given person minus how many people person trusts
    # Adjusted for 1-indexing
    counts = [0] * (N + 1)
    
    # Go through all relationships, incrementing trusted count and decrementing 
    # trustee count
    for truster, trustee in trust:
        counts[truster] -= 1
        counts[trustee] += 1
    
    # Check for someone whose count is N - 1
    for judge, count in enumerate(counts):
        if count == N - 1:
            return judge
    
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
