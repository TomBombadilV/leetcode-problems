# String to Integer (atoi)

from test import test

def myAtoi(s: str) -> int:
    # Dictionary of string to int of each digit 0-9
    nums = {}
    for i in range(10):
        nums[str(i)] = i

    n, signed = 0, False
    
    # Strip away all initial whitespace
    i = 0
    while i < len(s) and s[i] == " ": 
        i += 1

    # Check for plus or minus
    if i < len(s) and s[i] == "-":
        signed = True
        i += 1
    elif i < len(s) and s[i] == "+":
        i += 1
    else:
        pass

    # Add all digits to n. If non-digit found, break loop
    while i < len(s):
        if s[i] in nums:
            n *= 10
            n += nums[s[i]]
        else:
            break
        i += 1

    # Add signed bit
    n *= -1 if signed else 1

    # Check for max and min ints
    maxint, minint = 2 ** 31 - 1, -2 ** 31
    n = maxint if n > maxint else n
    n = minint if n < minint else n

    return n

cases = [("42", 42),
         ("4 2", 4),
         ("       -42", -42), 
         ("4192 with words", 4192),
         ("-91283472332", -2147483648),
         ("  2147483648", 2 ** 31 - 1),
         (" +42", 42),
         (" +-42", 0)
]
test(myAtoi, cases)
