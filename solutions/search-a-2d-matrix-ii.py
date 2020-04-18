# Search a 2D Matrix II

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
        

# Driver Code
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

"""m = []
m = [[]]"""

test_cases = [5, 1, 30, 15, 18, 100, -1]
expected = [True, True, True, True, True, False, False]
for case in test_cases:
    print(serachMatrix(m, case), expected)