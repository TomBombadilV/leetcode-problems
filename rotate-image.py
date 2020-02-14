# Rotate Image
# Time: O(n*n) | Space: O(n*n)

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        level = len(matrix) - i
        #print(i, level)
        for j in range(n - n//2):
            #print("[{0}][{1}] => [{2}][{3}] => [{4}][{5}] => [{6}][{7}]".format(i, j+i, level-1-j, i, level-1, level-1-j, j+i, level-1))
            temp = matrix[i][j]
            matrix[i][j] = matrix[~j][i]
            matrix[~j][i] = matrix[~i][~j]
            matrix[~i][~j] = matrix[j][~i]
            matrix[j][~i] = temp
        #print('----------- Level {0} ----------------'.format(level))
        #for n in m:
        #    print(n) 
        

m = [   [ 1,  2,  3,  4,  5,  6,  7], 
        [ 8,  9, 10, 11, 12, 13, 14], 
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48, 49]
    ]
m = [   [ 5,  1,  9, 11],
        [ 2,  4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]
    ]
"""m = [   [1, 2],
        [3, 4]
    ]
m = [   [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]"""
rotate(m)
for n in m:
    print(n)