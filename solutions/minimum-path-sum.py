
# Minimum Path Sum
# Use DP to fill a minimum sum path grid
# Time: O(n*m) | Space: O(n*m)
import sys
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    mins = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # If we're at the first square
            if i == 0 and j == 0:
                mins[i][j] = grid[i][j]
            # If we're at the first row (no squares above)
            elif i == 0 and j > 0:
                mins[i][j] = grid[i][j] + mins[i][j-1]
            # If we're at the first column (no squares to the left)
            elif j == 0 and i > 0:
                mins[i][j] = grid[i][j] + mins[i-1][j]
            # Regular squares, get the minimum between the top and left squares
            else:
                mins[i][j] = min(mins[i-1][j]+grid[i][j], mins[i][j-1]+grid[i][j])
    return mins[-1][-1]

case = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]
print(minPathSum(case))