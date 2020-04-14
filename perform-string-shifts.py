# Perform String Shifts
# Count up total amount of shifts, then perform shift
# Time: O(n) | Space: O(1)

from typing import List

def stringShift(s: str, shift: List[List[int]]) -> str:
    # Keep running total
    total = 0
    for sh in shift:
        # Get shift direction and amount from list
        direction, amount = sh
        # A shift to the left will be negative, shift to the right is positive
        direction = -1 if direction == 0 else 1
        # Add new shift to total
        total += direction * amount
    # No need to do shifts longer than length of string
    total = total % len(s)
    # An n shift to the left is equal to shift to the right len(s) - n times
    total = len(s) - total if total < 0 else total
    return s[-total:] + s[:-total]

# Driver code
cases = [   ("abc",         [[0, 1], [1, 2]]),
            ("abcdefg",    [[1, 1], [1, 1], [0, 2], [1, 3]])
]
for case in cases:
    s, shift = case
    print(stringShift(s, shift))
