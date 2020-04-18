# Palindrome Number
# Time: O(n) | Space: O(n) 

def isPalindrome(x: int) -> bool:
    # Negative case 
    if x < 0:
        return False
    # Turn integer into list
    l = []
    while x:
        l.append(x % 10)
        x = x // 10
    # Check opposing digits up to the middle
    mid = len(l) // 2
    for i in range(mid):
        # If digits are diferent, return False
        if not(l[i] == l[len(l) - i - 1]):
            return False
    return True

def isPalindrome(x: int) -> bool:
    # Negative case
    if x < 0:
        return False
    # Reverse integer
    temp = x
    rev = 0
    while temp:
        rev *= 10
        rev += temp % 10
        temp = temp // 10
    # Check if reversed int is same as original int
    return rev == x

# Driver code
cases = [121, -121, 10001, 1, 0, 1234, 123]
for case in cases:
    print("{0} is {1}a Palindrome".format(case, "not " if not(isPalindrome(case)) else ""))
