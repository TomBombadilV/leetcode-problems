# Permutation in String

from collections import Counter
from test import test

def checkInclusion(s1: str, s2: str) -> bool:
    perm_count = Counter(s1)
    start, end = 0, len(s1) - 1
    curr_count = Counter(s2[start:end + 1])
    while end < len(s2):
        if start > 0:
            curr_count[s2[end]] += 1
            curr_count[s2[start - 1]] -= 1
            if curr_count[s2[start - 1]] == 0:
                del curr_count[s2[start - 1]]
        if curr_count == perm_count:
            return True
        end += 1
        start += 1
    return False

# Driver Code
cases = [('ab', 'eidbaooo', True),
         ('ab', 'eidboaoo', False),
         ('a', 'ab', True),
         ('adc', 'dcda', True),
         ('cdd', 'dcda', True),
         ('a', 'a', True)
]
test(checkInclusion, cases)
