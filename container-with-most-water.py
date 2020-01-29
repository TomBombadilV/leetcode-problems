# Container With Most Water
# While maintaining the current max, move from the outermost points inward, 
# moving the pointer to the smaller value inward
# Time: O(n) | Space: O(1)

from typing import List

def maxArea(height: List[int]) -> int:
    # Start pointers at the beginning and end of the list
    ptr_a, ptr_b = 0, len(height) - 1
    max_area = 0
    while ptr_a != ptr_b:
        height_a, height_b = height[ptr_a], height[ptr_b]
        # Get the container area with the min of the two heights and the 
        # distance between them
        curr_area = (ptr_b - ptr_a) * min(height_a, height_b)
        # Compare current area and max area
        max_area = max(max_area, curr_area)
        # Move the pointer corresponding to the lower height
        if height_a < height_b:
            ptr_a+=1
        else:
            ptr_b-=1
    return max_area