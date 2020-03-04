# Number of Islands
# Iterate through matrix. Whenever an island is encountered, mark all of its connected parts as 0 and increment counter
# Time: O(m*n) | Space: O(1)

from typing import List

def delete_island(grid, i, j) -> int:
    if i > len(grid) - 1 or j > len(grid[0]) - 1 or i < 0 or j < 0:
        return
    if grid[i][j] == 1:
        grid[i][j] = 0
        delete_island(grid, i + 1, j)
        delete_island(grid, i, j + 1)
        delete_island(grid, i - 1, j)
        delete_island(grid, i, j - 1)

def numIslands(grid: List[List[int]]) -> int:
    n = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                delete_island(grid, i, j)
                n = n + 1
    return n

cases = [
    ([  [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], 1),
    ([  [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ], 3),
    ([], 0),
    ([[1],[1]], 1),
    ([  [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ], 1),
    ([[1,0,1,1,0,1,1]], 3)
]
for case in cases:
    grid, ans = case
    res = numIslands(grid)
    print("Passed" if res == ans else "Failed {1} expected {2}".format(res, ans))
