# Reverse Integer
# Get the sign, reverse the string of the absolute value int, make sure it's less than 2^31
# Time: O(n) | Space: O(n)

class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        i = str(abs(x))
        i = int(''.join(list(reversed(i))))
        return i * neg * (i < 2**31)