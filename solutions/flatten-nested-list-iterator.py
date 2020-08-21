# Flatten Nested List Iterator

from typing import List, Union

def flatten(l: List[Union[List, int]]) -> List[int]:
   for i, n in enumerate(l):
       print(i, n)
       if type(n) is list:
           f_n = flatten(n)
           l[i:i + 1] = f_n
   return l

def flatten(l: List[Union[List, int]]) -> List[int]:
    i = 0
    while i < len(l):
        if type(l[i]) is list:
            f_n = flatten(l[i])
            l[i:i + 1] = f_n
            i = i + len(f_n)
        else:
            i += 1
    return l

# Driver Code
cases = [[1, [1, 2, [3]], 2, 3],
         [[1], 2, 3],
         [1, 2, [3, 4]],
         [1, 2, []],
         [1, 2, [], 3, [[4, 5, [6]]]],
         [1, [2, [[], 3], [4], 5], 6, []],
         []
]
for case in cases:
    print(flatten(case))
