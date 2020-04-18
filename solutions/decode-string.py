# Decode String
# Regex? Woulda used a stack except I've been practicing regex lol

from re import match

def decodeString(s: str) -> str:
    res = ''
    while s:
        s, c = decodePart(s)
        res += c
    return res
    
def decodePart(s: str) -> str:
    p_1, p_2 = r'(\d+)\[([^\d\]]*)(.+)', r'([a-z]+)(.*)'
    m = match(p_1, s)
    if m:
        n, c, s = m.group(1), m.group(2), m.group(3)
    else:
        m_2 = match(p_2, s)
        n, c, s = 1, m_2.group(1), m_2.group(2)
    while s and s[0] != ']':
        s, c_2 = decodePart(s)
        c += c_2
    if m:
        s = s[1:]
    return s, c * int(n)

cases = ['3[a1[b]def]abc', '1[f]', '3[a]', '3[3[a]]', '3[a3[b]]', '3[a]3[b]', '3[a3[b]3[a]]3[a]', '', 'a', '3[a3[b]c]', '3[a]b', "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"]
for s in cases:
    print("{0} => {1}".format(s, decodeString(s)))