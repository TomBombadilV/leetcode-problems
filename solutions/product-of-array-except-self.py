# Product of Array Except Self
# For every n, calculate product of all nums from the left, then product of all 
# nums from the right. Product of array except self will be product of 
# right[i+1] and left[i-1]
# Time: O(n) | Space: O(n)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    # Get the product up until i from the left and right (padded)
    l, r = [1] * (n+2), [1] * (n+2)
    res = [1] * n
    # Multiply from the left
    for i in range(1, n+1):
        l[i] = nums[i-1] * l[i-1]
    # Multiply from the right
    for i in reversed(range(1, n+1)):
        r[i] = nums[i-1] * r[i+1]
    # Fill result array with product of left[i-1] and right[i+1] (account for 
    # padding)
    for i in range(n):
        res[i] = l[i] * r[i + 2]
    return res

def productExceptSelfConstanceSpace(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * (n+1)
    prod = 1
    for i in reversed(range(n)):
        prod = prod * nums[i]
        res[i] = prod
    prod = 1
    for i in range(n):
        res[i] = res[i+1] * prod
        prod = prod * nums[i]
    return res[:-1]



cases = [   [1, 2, 3, 4],
            [], 
            [1]
        ]
sols = [[24, 12, 8, 6], [], [1]]

for i, c in enumerate(cases):
    ans = productExceptSelfConstanceSpace(c)
    if ans == sols[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(c, ans, sols[i]))