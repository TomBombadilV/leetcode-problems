# Remove K Digits
# Method 1:
# Keep selecting the number of the highest order that is larger than the next.
# Time: O(n * k) | Space: O(1)
#
# Method 2:
# Run through the number string, selecting the peak and moving back by 1.
# Time: O(n) | Space: O(1)

from test import test

def removeKdigits(num: str, k: int) -> str:
    for _ in range(k):
        j = 0
        while j < len(num) - 1 and num[j] <= num[j + 1]:
            j += 1
        num = num[:j] + num[j + 1:]
        num = str(int(num)) if num else num
    return num if num else '0'

def removeKdigits(num: str, k: int) -> str:
    i, count = 0, 0
    while i < len(num) and count < k:
        j = i
        while j < len(num) - 1 and num[j] <= num[j + 1]:
            j += 1
        num = num[:j] + num[j + 1:] 
        num = str(int(num)) if num else num
        i = max(j - 1, 0)
        count += 1
    return num if num else '0' 

# Driver Code
cases = [('1432219', 3, '1219'),
         ('10200', 1, '200'),
         ('10', 2, '0'),
         ('1', 1, '0'),
         ('1', 0, '1'),
         ('12345', 1, '1234'),
         ('12345', 3, '12'),
         ('112', 1, '11')
#         ('111111122222223333333334444444445555555555', 20, None),
#         ('555555544444444433333333322222222211111111', 20, None)
]

test(removeKdigits, cases)
