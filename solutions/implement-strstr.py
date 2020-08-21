# Implement strStr()
# Keep checking every window of length of needle
# Time: O(n) | Space: O(n)

from test import test

def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1 if needle else 0

# Driver Code
cases = [('hello', 'll', 2),
         ('aaaaa', 'bba', -1)
]
test(strStr, cases)
