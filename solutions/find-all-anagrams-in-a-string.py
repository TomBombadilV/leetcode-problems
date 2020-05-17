# Find All Anagrams in a String
# Two pointer method
# Time: O(s * p) | Space: O(p)

from collections import Counter
from test import test
from typing import List

def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(p) > len(s) or len(s) == 0 or len(p) == 0:
        return []
    count = Counter(p)
    start = end = 0 
    res = []
    while start <= end and end < len(s):
        if s[end] in count:
            if count[s[end]] > 0:
                count[s[end]] -= 1
                if sum(count.values()) == 0:
                    res.append(start)
                    count[s[start]] += 1
                    start += 1
                end += 1
            else:
                count[s[start]] += 1
                start += 1
        else:
            start = end = end + 1 
            count = Counter(p)
    return res 

cases = [
    ('cbaebabacd', 'abc', [0, 6]),
    ('abab', 'ab', [0, 1, 2])
]
test(findAnagrams, cases)
