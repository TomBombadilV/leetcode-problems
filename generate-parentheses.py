# Generate Parentheses
# Keep count of opening parentheses and closed parentheses,
# Time: O(n) | Space: O(n)

from typing import List

def generateParentheses(n: int) -> List[str]:
    num_open, num_close = n, n
    solutions = ['']
    for _ in range(n * 2):
        print(num_open, num_close)
        add = []
        if num_close and num_close > num_open:
            add.append(')')
            num_close-=1
        if num_open:
            add.append('(')
            num_open-=1
        print('add: {0}'.format(add))
        solutions = [a + b for a in solutions for b in add]
    return solutions

for i in range(3):
    print("n: {0} -> {1}".format(i, generateParentheses(i)))