# Unique Paths
# For 1xn, there is 1 unique path. For 2xn, there are n unique paths. For 3xn, 
# there are 1+2+3+...+n
# 

from collections import defaultdict
from typing import Dict

def uniquePaths(m: int, n: int) -> int:
    # Keep track of how many paths can reach each square. Top left should be 1
    paths = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            # Since robot can only move right and down, check the squares to 
            # the left and up
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[-1][-1]

test_cases = [[3, 2], [7, 3], [1, 1], [2, 2], [100, 100]]
for case in test_cases:
    print("{0} => {1}".format(case, uniquePaths(case[0], case[1])))