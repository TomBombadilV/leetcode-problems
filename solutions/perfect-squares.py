# Perfect Squares
# Modified unbounded knapsack problem
# Time: O(n) | Space: O(n)

from math import floor, inf, sqrt

def numSquares(n: int) -> int:
    if n == 0:
        return 0
    res = [inf for i in range(n+1)]
    res[0] = 0
    # Calculate all possible squares
    squares = []
    sq = floor(sqrt(n))
    for i in range(sq):
        squares.append((i+1)**2)
    for i in range(n):
        for s in squares:
            if s <= i+1:
                res[i+1] = min(res[i+1], 1 + res[i+1-s])
    return res[-1]

cases = [12, 0, 1, 2, 100, 99]
sols = [3, 0, 1, 2, 1, 3]

for i, c in enumerate(cases):
    ans = numSquares(c)
    if ans == sols[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(c, ans, sols[i]))