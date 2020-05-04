# Roman to Integer
# Starting from the end of the string, if the current roman numeral is smaller 
# than the previous, subtract it from the sum. If not, add it to the sum.
# Time: O(n) | Space: O(1)

from test import test

def romanToInt(s: str) -> int:
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for i in reversed(range(len(s))):
        if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
            n -= dic[s[i]]
        else:
            n += dic[s[i]]
    return n

# Driver Code
cases = [('III', 3), ('IV', 4), ('IX', 9), ('LVIII', 58), ('MCMXCIV', 1994)]
test(romanToInt, cases)
