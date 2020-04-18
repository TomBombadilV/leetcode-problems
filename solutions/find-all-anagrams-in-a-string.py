# Find All Anagrams in a String
#
#

from collections import Counter
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    dic = Counter(p)
    res = []
    a_i = 0
    for i in range(len(s)):
        c = s[i]
        if c in dic and dic[c] > 0:
            dic[c] -= 1
            if sum(dic.values()) == 0:
                res.append(a_i)
                dic[a_i] += 1
                a_i += 1
        else:
            #if c in dic:
            #    dic[c] -= 1
            a_i = a_i + 1 if c in dic else i + 1
            dic = Counter(p)
    return res

cases = [
    ('cbaebabacd', 'abc', [0, 6]),
    ('abab', 'ab', [0, 1, 2])
]
for case in cases:
    s, p, ans = case
    res = findAnagrams(s, p)
    print("Passed" if res == ans else "Failed with {1} expected {2}".format(res, ans))