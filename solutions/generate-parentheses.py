# Generate Parentheses
# Backtraaaaack
# Time: O(2^n) | Space: O(n^2)

from typing import List

def generateParentheses(n: int) -> List[str]:
    # 2n is the total length of the string
    return recurse(n*2, '', n, n, [])

def recurse(n: int, s: str, opens_left: int, closes_left: int, solutions: List[str]) -> List[str]:
    if n <= 1:
        # If we have more opens than closes so far, then we have a complete string
        if opens_left == 0 and closes_left == 1:
            solutions.append(s + ')')
        return solutions
    # We can only add brackets if we have more opening brackets than closing brackets so far
    if opens_left <= closes_left:
        recurse(n-1, s+'(', opens_left-1, closes_left, solutions)
        recurse(n-1, s+')', opens_left, closes_left-1, solutions)
    return solutions

for i in range(5):
    print("{0} => {1}".format(i, generateParentheses(i)))