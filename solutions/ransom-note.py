# Ransom Note
# Add all letters and their count in magazine to a dictionary. Then run through
# ransom note and make sure enough letters exist.
# Time: O(m + n) | Space: O(m)

from collections import Counter
from test import test
from typing import List

def canConstruct(ransomNote: str, magazine: str) -> bool:
    dic = Counter(list(magazine))
    for c in ransomNote:
        if dic[c] < 1:
            return False
        dic[c] -= 1
    return True

# Driver Code
cases = [('a', 'b', False), ('aa', 'ab', False), ('aa', 'aab', True)]
test(canConstruct, cases)
