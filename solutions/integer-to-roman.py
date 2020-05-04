# Integer to Roman
# Method 1:
# Generalized solution where digits that are 1 or 0 difference from 5 or 10
# are represented with 5 or 10 symbol minus 1 or 0. Other numbers are 
# represented by x number of "1"s in the current order.
#
# Method 2:
# Hard code "minus 1" numbers, then keep adding the corresponding numerals 
# from highest to lowest

from test import test

def intToRoman(num: int) -> str:
    """
    Method 1
    """
    # Only works for numbers representable by Roman numeral system
    if num < 1 or num > 3999:
        return ''

    # Map digit to roman numeral
    roman = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
   
    n, res, order = num, '', 1
    while n:
        # Chunk of numerals currently being added to result
        add = ''
        
        # Strip each digit off end of number
        digit = n % 10
        n = n // 10
        
        # Based off 5 or 10
        rounded = 5 if digit <= 5 else 10
        
        # If more than 1 away from base, add base - 5 and remaining number of 1s
        if rounded - digit > 1:
            add += roman[(rounded - 5) * order]
            add += roman[order] * (digit - (rounded - 5))
        
        # If 1 or 0 away from base, add 1 and base
        else:
            add += roman[order] * (rounded - digit)
            add += roman[rounded * order]
        
        # Update order
        order *= 10

        # Add to beginning of result
        res = add + res
    return res

def intToRoman(num: int) -> str:
    """
    Method 2
    """
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    digit = [ 1000, 900, 500, 400,  100,  90,  50,  40,   10,  9,    5,   4,    1 ] 
    res = ''
    for r, d in zip(roman, digit):
        res += r * (num // d)
        num %= d
    return res

# Driver code
cases = [(3, 'III'), (4, 'IV'), (9, 'IX'), (58, 'LVIII'), 
         (1994, 'MCMXCIV'), (99, 'XCIX'), (1, 'I'), (10, 'X'),
         (50, 'L'), (49, 'XLIX')]
test(intToRoman, cases)
