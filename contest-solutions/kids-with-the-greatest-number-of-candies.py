# Kids With the Greatest Number of Candies
# Find the max in the candy array, then find the difference between each amount
# and the max. Finally, compare each diff with the amount of extra candies.
# Time: O(n) | Space: O(n)

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # Get highest number of candies
    max_c = max(candies)
    # Find difference between each amount and the max
    diff = [max_c - c for c in candies]
    # Check if each diff can be made up by amount of extra candies
    res = [False] * len(candies)
    for i in range(len(candies)):
        if diff[i] <= extraCandies:
            res[i] = True
    return res

# Driver Code
cases = [   ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
            ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
            ([12, 1, 12], 10, [True, False, True])
]
for case in cases:
    candies, extraCandies, expected = case
    res = kidsWithCandies(candies, extraCandies)
    print("Passed" if res == expected else "{0} failed with {1} expected {2}".\
          format((candies, extraCandies), res, expected))
