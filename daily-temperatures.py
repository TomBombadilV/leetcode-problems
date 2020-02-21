# Daily Temperatures
# idk I think I'm stupid or mentally impaired
# Time: O(n) | Space: O(n)

from typing import List

def dailyTemperatures(T: List[int]) -> List[int]:
    stack = []
    res = [0] * len(T)
    for i in range(len(T)):
        # If curr is larger than stack item
        if stack and T[i] > stack[-1][0]:
            # While curr is larger than stack item, pop and set its days
            while stack and T[i] > stack[-1][0]:
                _, j = stack.pop()
                res[j] = i - j
        # Save stack item and its index
        stack.append((T[i], i))
    return(res)

test_cases = [  [73, 74, 75, 71, 69, 72, 76, 73],
                [0, 0, 0],
                [],
                [1, 2],
                [3, 2, 1]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, dailyTemperatures(case)))