# Climbing Stairs
# Basically Fibonacci, because from any step n, you can take one step to it 
# from n-1 and two steps to it from n-2
# Time: O(n) | Space: O(1)

def climbStairs(n: int) -> int:
    i, j = 0, 1
    for _ in range(n):
        j, i = i + j, j
    return j

for case in range(6):
    print("{0} => {1}".format(case, climbStairs(case)))