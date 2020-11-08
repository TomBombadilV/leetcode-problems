# Consecutive Characters

from test import test

def max_power(s: str) -> int: 
    """ Iterate through string, checking if current char matches
        previous char, keeping track of current continuous substring.
        Time: O(n) | Space: O(1)
    """
    curr_len, max_len = 1, 1
    for i in range(1, len(s)):
        # If doesn't match previous character, reset count
        if not s[i] == s[i - 1]:
            curr_len = 1
        # Or else, increment count
        else:
            curr_len += 1
        # Check if new current length improves on max length
        max_len = max(curr_len, max_len)
    return max_len

# Driver Code
cases = [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("triplepillooooow", 5),
    ("hooraaaaaaaaaaay", 11),
    ("tourist", 1)
]
#test(max_power, [cases[0]])
test(max_power, cases)
