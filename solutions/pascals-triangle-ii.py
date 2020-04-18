# Print the kth row of Pascal's Triangle

from typing import List

def getRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    prev = getRow(rowIndex - 1)
    prev = [0] + prev + [0]
    return [prev[i - 1] + prev[i] for i in range(1, len(prev))]

# Driver Code
for i in range(10):
    print(getRow(i))
