# Count and Say

def countAndSay(n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        new_s = ''
        count, prev = 0, ''
        for c in s:
            if not(c == prev):
                new_s += str(count) + prev if count > 0 else ''
                prev = c
                count = 0
            count += 1
        new_s += str(count) + prev
        s = new_s
    return s

# Driver Code
countAndSay(10)
