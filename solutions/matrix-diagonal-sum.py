# Matrix Diagonal Sum

from typing import List

def diagonal_sum(mat: List[List[int]]) -> int:
    # Sum diags row by row (0 + i, 0 - i)
    res = sum([mat[i][i] + mat[i][(len(mat) - 1) - i] for i in range(len(mat))])
    # If matrix has odd length, then center square was counted twice
    return res if len(mat) & 1 == 0 else res - mat[len(mat) // 2][len(mat) // 2] 

# Driver Code
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonal_sum(mat))

mat = [[1,1,1,1],
      [1,1,1,1],
      [1,1,1,1],
      [1,1,1,1]]
print(diagonal_sum(mat))
