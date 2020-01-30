# Letter Combinations of a Phone Number
# Fill strings one letter at a time from dictionary
# Time: O(n) | Space: O(n^2)

from typing import List

def letterCombinations(digits: str) -> List[str]:
    # Put the letters corresponding to each number into dictionary
    dic = { '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
    # If digits is an empty string, return empty list
    combos = [''] if digits else []
    # Iterate through digit list
    for i in range(len(digits)):
        # Add new digits through nested for loop
        combos = [ a + b for a in combos for b in dic[digits[i]]]
    return combos