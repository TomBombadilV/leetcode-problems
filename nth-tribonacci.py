# Nth Tribonacci Number
# Practicing recursion with memoization

from collections import defaultdict

def tribonacci(n: int) -> int:
    dic = defaultdict(int)
    dic[0], dic[1], dic[2] = 0, 1, 1
    return tribonacci_helper(n, dic)

def tribonacci_helper(n: int, dic) -> int:
    if n in dic:
        return dic[n]
    else:
        trib = tribonacci_helper(n-3, dic) + tribonacci_helper(n-2, dic) + tribonacci_helper(n-1, dic)
        dic[n] = trib
        return trib

print(tribonacci(28))