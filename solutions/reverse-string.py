# Reverse a string in place recursively

from typing import List

def reverseString(s: List[str]) -> None:
    # Number of swaps we need to make
    n = len(s) // 2
    return reverse_string_util(s, n)

def reverse_string_util(s: List[str], n: int) -> None:
    # No more swaps needed
    if n == 0:
        return s
    # Swap character at current index and its opposite
    s[n - 1], s[len(s) - n] = s[len(s) - n], s[n - 1]
    # Recurse
    return reverse_string_util(s, n - 1)

s = 'hello'
s_list = list(s)
print(reverseString(s_list))
