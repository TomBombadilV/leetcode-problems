# Leftmost Column with at Least a One
# ----------------------------------- Note -------------------------------------
# Quite possibly the most pedantic, unncessary question setup while still being
# poorly written. 
# Would be a rather good question if the author could get his/her head out of
# the sand and calm down a little bit.
# ------------------------------------------------------------------------------
# Method 1 
# For each column, find the index of the first 1 using binary search. Keep track
# of minimum.
# Time: O(m * logn) | Space: O(1)
#
# Method 2
# Iteratively run through each row, stopping when encountering a 0 and hopping to 
# the next row
# Time: O(m + n) | Space: O(1)
# 
# Method 3
# Alternatively, use Method 1 but only search parts of array that have indices 
# smaller than current minimum.
# Time: O(logm + n) | Space: O(1)

from typing import List

# Method 1
def leftMostColumnWithOne(binaryMatrix: List[List[int]]) -> int:
    # Returns index of first instance of 1 in row
    def rows_first_one(row: List[int]) -> int:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            # If 1 is at beginning of row or is right after a 0, it's the first
            if row[mid] == 1 and (mid == 0 or row[mid - 1] == 0):
                return mid
            # If it's a 0, look on the right
            elif row[mid] == 0:
                left = mid + 1
            # If it's a 1 but not the first, look on the left
            else:
                right = mid - 1
        # Return -1 if no 1 found in row
        return -1
   
    # Keep track of smallest index. -1 if no 1s found
    min_i = -1
    # Get each row's first 1 index
    for row in binaryMatrix:
        res = rows_first_one(row)
        # Check if min_i exists yet and if 1 exists in row
        min_i = res if min_i == -1 or (res < min_i and res > -1) else min_i
    return min_i

# Method 3
def leftMostColumnWithOne(binaryMatrix: List[List[int]]) -> int:
    # Returns index of first instance of 1 in window of row where upper bound is 
    # current min index
    def rows_first_one(row: List[int], min_i) -> int:
        left = 0
        # If min index is valid (not -1), set right ptr to min index
        right = min_i - 1 if min_i > -1 else len(row) - 1 
        # Perform binary search to find first index of 1 within given window
        while left <= right:
            mid = (left + right) // 2
            # If 1 is at beginning of row or is right after a 0, it's the first
            if row[mid] == 1 and (mid == 0 or row[mid - 1] == 0): 
                return mid
            # If 0, look on the right
            elif row[mid] == 0:
                left = mid + 1 
            # If 1, look on the left
            else:
                right = mid - 1 
        # Return -1 if no 1 found in window
        return -1
   
    # Keep track of smallest index. -1 if no 1s found
    min_i = -1
    # Check whether each row has a 1 in a position smaller than current min
    for row in binaryMatrix:
        res = rows_first_one(row, min_i)
        # Check if min_i exists yet and if 1 exists in window
        min_i = res if min_i == -1 or (res < min_i and res > -1) else min_i
    return min_i

# Translated to fit problem's totally inane "interactive interface"
def leftMostColumnWithOne_leetcode(self, binaryMatrix: 'BinaryMatrix') -> int:
    # Takes in matrix, row length, row index, and current min index. Returns 
    # index of first 1
    def rows_first_one(mat: 'BinaryMatrix', m: int, row_i: int, min_i: int) -> int:
        left = 0
        # If min index is valid (not -1), set right ptr to min index
        right = min_i - 1 if min_i > -1 else m - 1
        # Perform binary search to find first index of 1 within given window
        while left <= right:
            mid = (left + right) // 2
            # Minimize number of get calls lol
            mid_val = mat.get(row_i, mid)
            if mid_val == 1 and (mid == 0 or mat.get(row_i, mid - 1) == 0):
                return mid
            elif mid_val == 0:
                left = mid + 1
            else:
                right = mid - 1
        # Return -1 if no 1 found in window
        return -1

    # Get dimensions of binary matrix
    n, m = binaryMatrix.dimensions()
    # Keep track of minimum index
    min_i = -1
    # Go through each row and find its minimum 1 index
    for i in range(n):
        res = rows_first_one(binaryMatrix, m, i, min_i)
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
