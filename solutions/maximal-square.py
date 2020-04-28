# Maximal Square
# Method 1
# For each index in the matrix, explore the largest square possible from that 
# position by continuously exploring down, diagonally, and to the right. If an
# index is moved to diagonally, continue diagonally. If moved to from above,
# continue by looking diagonally and down. If moved to from the left, continue
# looking to the right and diagonally.
# Time: O(m * n) | Space: O(1)
#
# Method 2
# Use DP to fill in a max area matrix corresponding to each index in the 
# original matrix. Find max area for each index as the bottom right corner of
# potential square, so look at indices to the left, above, and upper left.
# Time: O(m * n) | Space: O(m * n)

from typing import Dict, List

# Method 1
def maximalSquare(matrix: List[List[str]]) -> int:
    
    # Check down, right, and diagonal
    def checkSquare(m: List[List[str]], i: int, j: int) -> bool:
        if i > len(m) - 1 or j > len(m[0]) - 1 or not(m[i][j]) or m[i][j] == "0":
            return 0
        # Get max lengths traversing down, right, and diagonal
        down = checkDown(m, i + 1, j)
        right = checkRight(m, i, j + 1)
        diag = checkDiag(m, i + 1, j + 1)
        # Max area will be the smallest of the three (max length) squared (to 
        # get area)
        return (1 + min(down, right, diag)) ** 2

    # Check down will check down and diagonal
    def checkDown(m, i, j): 
        if i > len(m) - 1 or j > len(m[0]) - 1 or not(m[i][j]) or m[i][j] == "0":
            return 0
        return 1 + min(checkDown(m, i + 1, j), checkDiag(m, i + 1, j + 1)) 
    
    # Check to the right and diagonal
    def checkRight(m, i, j): 
        if i > len(m) - 1 or j > len(m[0]) - 1 or not(m[i][j]) or m[i][j] == "0":
            return 0
        return 1 + min(checkRight(m, i, j + 1), checkDiag(m, i + 1, j + 1)) 
    
    # Check only diagonal
    def checkDiag(m, i, j): 
        if i > len(m) - 1 or j > len(m[0]) - 1 or not(m[i][j]) or m[i][j] == "0":
            return 0
        return 1 + checkDiag(m, i + 1, j + 1)

    max_area = 0 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 or matrix[i][j] == "1":
                max_area = max(max_area, checkSquare(matrix, i, j)) 
    return max_area

# Method 2
def maximalSquare(matrix: List[List[str]]) -> int:
    # Empty matrix, no squares!!
    if not(matrix):
        return 0
    m, n = len(matrix), len(matrix[0])
    # Max square length for every index in matrix
    max_l = [[0 for _ in range(n)] for _ in range(m)]
    # Keep track of current max length
    max_len = 0
    for i in range(m):
        for j in range(n):
            # Max length will be min of top, left, and upper left diagonal (plus self)
            if matrix[i][j] == '1' or matrix[i][j] == 1:
                max_l[i][j] = min(max_l[i - 1][j], max_l[i][j - 1], max_l[i - 1][j - 1]) + 1
                max_len = max(max_len, max_l[i][j])
    # Area is length squared
    return max_len ** 2

# Driver Code
cases = [
    ([[1, 0, 1, 0, 0],
      [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 0, 0, 1, 0]], 4),
    ([], 0),    
    ([[1]], 1),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]], 9),
    ([[0, 1, 1],
      [1, 1, 1],
      [1, 1, 1]], 4),
    ([[1, 0, 1, 0, 0],
      [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 0, 0, 1, 0]], 4),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 0]], 9),
    ([[1, 0, 1, 0, 0],
      [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 0, 0, 1, 0]], 4),
    ([[0, 1, 1, 0, 1],
      [1, 1, 0, 1, 0],
      [0, 1, 1, 1, 0],
      [1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0]], 9)
]

for case in cases:
    grid, ans = case
    res = maximalSquare(grid)
    print("Passed" if res == ans else "Failed {0} expected {1}".format(res, ans))
