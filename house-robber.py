# House Robber
# Deeeee peeeeee
# Time: O(n) | Space: O(n)

from typing import List

def rob(nums: List[int]) -> int:
    m = [0] * (len(nums) + 2)
    for i, n in enumerate(nums):
        m[i+2] = max(m[i], m[i-1]) + n
    return max(m)

def rob_better(nums: List[int]) -> int:
    one_back, two_back, three_back = 0, 0, 0
    sol = 0
    for n in nums:
        temp = one_back
        one_back = max(two_back, three_back) + n
        three_back, two_back = two_back, temp
        sol = max(sol, one_back)
    return sol

cases = [   [1, 2, 3, 1],
            [2, 7, 9, 3, 1],
            [],
            [100, 0, 0, 100],
            [1, 2, 3, 4, 5],
            [0],
            [1],
            [1, 2],
            [1, 2, 3]
        ] 
sols = [4, 12, 0, 200, 9, 0, 1, 2, 4]
for i, c in enumerate(cases):
    ans = rob_better(c)
    if ans == sols[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(c, ans, sols[i]))