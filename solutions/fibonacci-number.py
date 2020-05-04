# Fibonacci Number
# Method 1:
# Recursion with memoization
# Method 2:
# Iterative method

from typing import Dict

def fib(N: int) -> int:
    """
    Method 1
    """
    dic = {}
    dic[0] = 0
    dic[1] = 1

    def recurse(dic: Dict[int, int], n: int) -> int:
        if n in dic:
            return dic[n]
        res = recurse(dic, n - 1) + recurse(dic, n - 2)
        dic[n] = res
        return res

    return recurse(dic, N)

def fib(N: int) -> int:
    """
    Method 2
    """
    i, j = 0, 1
    for _ in range(N):
        i, j = j, i + j
    return j

for i in range(20):
    print(fib(i))
