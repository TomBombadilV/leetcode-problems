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
    # The number of solutions is the number of possible letters for each digit 
    # multiplied together
    combos = []
    for digit in digits:
        combos += [''] * len(dic[digit])
    
    for i in range(len(digits)):
        # Current digit
        digit = digits[i]
        # Get the number of digits in the string before and after this one
        num_prev_digits, num_following_digits = i, len(digits) - i - 1
        # Letters corresponding to current digit
        letters = dic[digit]
        print(digit, num_prev_digits, num_following_digits, letters)
        for j in range(len(letters)):
            #combos[] + letters[j]
            for k in range(num_prev_digits):
                for l in range(num_following_digits):
                    print(letters[j], k, l)

letterCombinations('234')