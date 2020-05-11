# Flood Fill
# DFS
# Time: O(m * n) | Space: O(1)

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int)\
    -> List[List[int]]:
    
    def fill(image: List[List[int]], sr: int, sc: int, newColor: int, 
             origColor: int) -> List[List[int]]:
        if not(image) or sr < 0 or sc < 0 or sr >= len(image) or\
            sc >= len(image[0]) or image[sr][sc] == newColor or\
            not(image[sr][sc] == origColor):
            return image
        image[sr][sc] = newColor
        image = fill(image, sr, sc - 1, newColor, origColor)  # Left
        image = fill(image, sr, sc + 1, newColor, origColor)  # Right
        image = fill(image, sr - 1, sc, newColor, origColor)  # Above
        image = fill(image, sr + 1, sc, newColor, origColor)  # Below
        return image

    return fill(image, sr, sc, newColor, image[sr][sc])

# Driver Code
image = [[0,0,0],[0,1,1]]
sr, sc, newColor = 1, 1, 1
print(floodFill(image, sr, sc, newColor))
