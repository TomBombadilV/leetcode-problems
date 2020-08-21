# Add Binary
# Add two binary numbers together

def addBinary(a: str, b: str) -> str:
    (a, b) = (a, b) if len(a) >= len(b) else (b, a)
    res, carry = '', 0
    i = 1
    while i <= len(b):
        carry += int(a[-i]) + int(b[-i])
        res =  str(carry % 2) + res
        carry //= 2
        i += 1
    while i <= len(a):
        carry = int(a[-i]) + carry
        res = str(carry % 2) + res
        carry //= 2
        i += 1
    res = ('1' if carry else '') + res
    return res

def addBinary(a: str, b: str) -> str:
    res, carry = '', 0
    a, b = list(a), list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        res = str(carry % 2) + res
        carry //= 2

    print(res)
    return res
    
# Driver Code
addBinary('11', '1')
addBinary('1010', '1011')
