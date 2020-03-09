# Decode String
# 
#

import re

def decodeString(s: str) -> str:
    res = ''
    while s:
        if isDigit(s[0]):
            p = r'(\d+)\[([^\d\[\]]*)(.+)'
            match = re.match(p, s)
            repeater, repeatee, remaining = int(match.group(1)), match.group(2), match.group(3)
            print(repeater, repeatee, remaining)
            if remaining[0] == ']':
                remaining = remaining[1:]
                res = res + (repeatee * repeater)
            else:
                print(decodeString(remaining))

#def decode(s:str) -> str:


#s = str(input('Enter a string: '))
cases = ['3[a]', '3[a3[b]]', '3[a]3[b]']
for s in cases:
    print(s)
    print('---------------')
    decodeString(s)
    print()