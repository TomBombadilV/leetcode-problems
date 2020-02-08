# Unique Paths
# Use nCr for the number of "right" and "down" moves you need to make

import operator as op
from functools import reduce

def uniquePaths(m: int, n: int) -> int:
    return int(ncr(m+n-2, n-1))

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom