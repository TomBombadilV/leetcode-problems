# Plus One
# Time: O(n) | Space: O(1)

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    # Start with carry 1 because we're adding 1 to the original number
    carry = 1
    # Starting from the end of the list, add 1
    for i in reversed(range(len(digits))):
        # If carry is 0, we can stop since rest of the list will be the same
        if carry == 0:
            return digits
        # Maffs is all around us
        curr_sum = carry + digits[i]
        # Calculate the carry
        carry = 1 if curr_sum > 9 else 0
        # Update list
        digits[i] = curr_sum % 10
    # If we have a carry left, add 1 to the beginning of the list
    if carry:
        digits = [1] + digits
    return digits

test_cases = [  [1, 2, 3],
                [4, 3, 2, 1],
                [9, 9, 9]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, plusOne(case)))