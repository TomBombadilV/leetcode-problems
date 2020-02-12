# Daily Temperatures
# idk I think I'm stupid or mentally impaired

from typing import List

def dailyTemperatures(T: List[int]) -> List[int]:
    l = []
    for i in range(len(T)-1):
        j = 1
        next_temp = T[i+j]
        while T[i] >= next_temp and i+j < len(T)-1:
            j+=1
            next_temp = T[i+j]
        if T[i] < next_temp:
            l.append(j)
        else:
            l.append(0)
    l.append(0)
    return l

test_cases = [  [73, 74, 75, 71, 69, 72, 76, 73],
                [0, 0, 0],
                [],
                [1, 2],
                [3, 2, 1]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, dailyTemperatures(case)))