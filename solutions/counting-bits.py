# Counting Bits
# Method 1:
# Isolate all bits beside leading bit, then add 1
#
# Method 2:
# Divide by 2 to remove last bit, then add 1 if number is odd

from math import log
from typing import List

def countBits(num: int) -> List[int]:
    res = [0 for _ in range(num + 1)]
    for i in range(1, num + 1):
        base = int(log(i, 2))
        inc = i - (2 ** base)
        res[i] = res[inc] + 1
    return res

def countBits(num: int) -> List[int]:
    res = [0 for _ in range(num + 1)]
    for i in range(1, num + 1):
        res[i] = res[i // 2] + (i % 2)
    return res

print(countBits(32))
