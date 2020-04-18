# Number of Islands

from typing import List

def delete_island(grid: List[List[str]], i: int, j: int) -> None:
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
        grid[i][j] = '0'
        delete_island(grid, i - 1, j)
        delete_island(grid, i + 1, j)
        delete_island(grid, i, j - 1)
        delete_island(grid, i, j + 1)
    return grid

def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                grid = delete_island(grid, i, j)
    return count

# Driver code
g = [   ['1', '1', '1', '1', '0'],
        ['1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
]
g = [   ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
]

print(numIslands(g))
