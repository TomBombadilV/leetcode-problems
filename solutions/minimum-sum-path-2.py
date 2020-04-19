# Minimum Path Sum
# At each index, look at indices to the top and to the left and pick the smaller  
# value. Greedy choice at each step will lead to optimal solution
# Time: O(m * n) | Space: O(1)

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    # Iterate through entire graph
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If no squares above
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j - 1]
            # If no squares to the left
            elif i > 0 and j == 0:
                grid[i][j] += grid[i - 1][j]
            # Have squares to the left and to the top, pick min
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            # If i == 0 and j == 0 aka we're in the upper left corner with no
            # left or upper indices
            else:
                pass
    # Return bottom right min path
    return grid[-1][-1]

# Driver code
g = [   [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
]

print(minPathSum(g))
