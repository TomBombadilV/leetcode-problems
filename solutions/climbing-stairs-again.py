from typing import Dict 

def climbStairs(n: int) -> int:
        dic = {}
        dic[0] = 0
        dic[1] = 1
        dic[2] = 2
        
        def recurse(dic: Dict[int, int], n: int) -> int:
            if n in dic:
                return dic[n]
            res = recurse(dic, n - 2) + recurse(dic, n - 1)
            dic[n] = res
            return res
        
        return recurse(dic, n)
           
print(climbStairs(4))
