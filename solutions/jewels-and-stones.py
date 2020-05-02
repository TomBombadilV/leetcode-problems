# Jewels and Stones
# Add all jewels into a hashset. Iterate through string and increment counter if
# stone exists in jewel set.
# Time: O(J + S) | Space: O(J)

def numJewelsInStones(J: str, S: str) -> int:
    # Add jewels to set
    jewels = set(list(J))
    # Count all stones that are jewels
    res = 0
    for s in S:
        if s in jewels:
            res += 1
    return res

# Driver Code
cases = [ ('aA', 'aAAbbbb'),
          ('z', 'ZZ')
]
for case in cases:
    J, S = case
    print(numJewelsInStones(J, S))
