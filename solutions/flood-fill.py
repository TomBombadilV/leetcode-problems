# Flood Fill
# DFS
# Time: O(m * n) | Space: O(1)

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int)\
    -> List[List[int]]:
    
    def fill(image: List[List[int]], sr: int, sc: int, newColor: int, 
             origColor: int) -> List[List[int]]:
        # Check if indices out of bounds or if color is already new color
        # or color is not original color
        if not(image) or sr < 0 or sc < 0 or sr >= len(image) or\
            sc >= len(image[0]) or image[sr][sc] == newColor or\
            not(image[sr][sc] == origColor):
            return image

        # Set new color
        image[sr][sc] = newColor

        # Look up, down, left and right
        image = fill(image, sr, sc - 1, newColor, origColor)  # Left
        image = fill(image, sr, sc + 1, newColor, origColor)  # Right
        image = fill(image, sr - 1, sc, newColor, origColor)  # Up
        image = fill(image, sr + 1, sc, newColor, origColor)  # Down
        return image

    return fill(image, sr, sc, newColor, image[sr][sc])

# Driver Code
image = [[0,0,0],[0,1,1]]
sr, sc, newColor = 1, 1, 1
print(floodFill(image, sr, sc, newColor))
