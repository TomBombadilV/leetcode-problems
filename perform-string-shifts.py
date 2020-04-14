# Perform String Shifts
# Count up total amount of shifts, then perform shift
# Time: O(n) | Space: O(1)

from typing import List

def stringShift(s: str, shift: List[List[int]]) -> str:
    # Keep running total
    total = 0
    for direction, amount in shift:
        # Negative if to the left else positive to the right
        total += -amount if direction == 0 else amount
    # No need to do shifts longer than length of string
    total = total % len(s)
    # Apply shift
    return s[-total:] + s[:-total]

# Driver code
cases = [   ("abc",         [[0, 1], [1, 2]]),
            ("abcdefg",    [[1, 1], [1, 1], [0, 2], [1, 3]])
]
for case in cases:
    s, shift = case
    print(stringShift(s, shift))
