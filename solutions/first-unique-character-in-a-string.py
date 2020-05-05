# First Unique Character in a String
# Count number of instances of each character. Then iterate through and return
# first character with count of 1

from collections import Counter

def firstUniqChar(s: str) -> int:
    count = Counter(list(s))
    for c in s:
        if count[c] == 1:
            return c
    return None
