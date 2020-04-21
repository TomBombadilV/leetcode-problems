# Leftmost Column with at Least a One
# Quite possibly the most pedantic, unncessary question setup while still being
# extremely poorly written. 
# Would be a rather good question if the author could get his/her head out of
# the sand and calm down a little bit.
# 
# For each column, find the index of the first 1 using binary search. Keep track
# of minimum. Alternatively, only search parts of array that have indices smaller
# than current minimum.
# Time: O(m * logn) | Space: O(1)

from typing import List

def leftMostColumnWithOne(binaryMatrix: List[List[int]]) -> int:
    def rows_first_one(row: List[int]) -> int:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == 1 and (mid == 0 or row[mid - 1] == 0):
                return mid
            elif row[mid] == 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    min_i = -1
    for row in binaryMatrix:
        res = rows_first_one(row)
        min_i = res if min_i == -1 or (res < min_i and res > -1) else min_i
    return min_i

# Translated to fit problem's totally inane "interactive interface"
def leftMostColumnWithOne_leetcode(self, binaryMatrix: 'BinaryMatrix') -> int:
    def rows_first_one(mat: 'BinaryMatrix', m: int, row_i: int) -> int:
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mat.get(row_i, mid)
            if mid_val == 1 and (mid == 0 or mat.get(row_i, mid - 1) == 0):
                return mid
            elif mid_val == 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    n, m = binaryMatrix.dimensions()
    min_i = -1
    for i in range(n):
        res = rows_first_one(binaryMatrix, m, i)
        min_i = res if min_i == -1 or (res < min_i and res > -1) else min_i
    return min_i

# Driver code
cases = [   [[0, 0],
             [1, 1]],

            [[0, 0],
             [0, 1]],

            [[0, 0],
             [0, 0]],

            [[0, 0, 0, 1],
             [0, 0, 1, 1],
             [0, 1, 1, 1]],
            
            [[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1],[0,0,0,0,1],[0,0,0,0,0]]
]
for case in cases:
    print(leftMostColumnWithOne(case))
