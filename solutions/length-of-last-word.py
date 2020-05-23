# Length of Last Word
# Split string by spaces. Iterate from back to front, checking for a
# nonempty string. If iterates past length of string, return 0
# Time: O(n) | Space: O(n)

from test import test

def lengthOfLastWord(s: str) -> int:
    l = s.split(' ')
    i = 1
    while i <= len(l) and not(l[-i]):
        i += 1
    return len(l[-i]) if i <= len(l) else 0

# Driver Code
cases = [(' ', 0), ('a     ', 1), ('', 0)]
test(lengthOfLastWord, cases)
