# Longest Common Prefix

from test import test
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # Make sure strs is not empty
    if not(strs): 
        return ''
    res = ''
    # Iterate through first string in strs
    for i, c in enumerate(strs[0]):
        # Check each char against all other strings
        for s in strs:
            # If end of string passed or character doesn't match
            if i > len(s) - 1 or not(s[i] == c):
                return res
        res += curr
    return res

# Driver Code
cases = [(['flower', 'flow', 'flight'], 'fl'),
         (['dog', 'racecar', 'car'], ''),
         (['a', 'ab', 'abc'], 'a')
]
test(longestCommonPrefix, cases)
