# Trapping Rain Water
# Save max height from left and right to calculate how much can be stored at each point
#Time: O(n) | Space: O(n)

from typing import List

def trap(height: List[int]) -> int:
    max_height = [0] * len(height)
    res = 0
    max_h = 0
    for i in range(len(height)):
        max_h = max(max_h, height[i])
        max_height[i] = max_h
    max_h = 0
    for i in reversed(range(len(height))):
        max_h = max(max_h, height[i])
        max_height[i] = min(max_h, max_height[i])
        res = res + max_height[i] - height[i]
    return res

h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))