# Maximal Square
# Deee peee
# Time: O(m * n) | Space: O(m * n)

from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:
    max_sq = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                #print(i, j, matrix[i - 1][j], matrix[i][j - 1])
                left = min(matrix[i - 1][j][1] + 1, matrix[i][j - 1][0] + 1)  if i > 0 else matrix[i][j]
                right = matrix[i][j - 1][0] + 1 if j > 0 else matrix[i][j]
                matrix[i][j] = (left, right)
                if i == 1 and j ==3:
                    print(matrix[i - 1][j], matrix[i][j - 1], matrix[i][j])
                curr_max = max(matrix[i][j][0], matrix[i][j][1])
                max_sq = max(max_sq, curr_max)
            else:
                matrix[i][j] = (0, 0)
    return max_sq

cases = [
    ([[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]], 4),
    ([], 0),    
    ([[1]], 1),
    ([[1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]], 3),
    ([[0, 1, 1],
    [1, 1, 1],
    [1, 1, 1]], 2)
]

cases = [
    ([[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]], 4)]

for case in cases:
    grid, ans = case
    res = maximalSquare(grid)
    print("Passed" if res == ans else "Failed {0} expected {1}".format(res, ans))
