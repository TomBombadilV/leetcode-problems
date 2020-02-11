# Largest Rectangle in Histogram
# Starting at the leftmost bar, keep track of the largest rectangle that can be
# made with the current bar
# Time: O(n^2) | Space: O(1)

def largestRectangleArea(heights: List[int]) -> int:
    max_area = 0
    for i, bar in enumerate(heights):
        # We only need to make a calculation if bar is taller than previous bar
        if bar > heights[i-1]:
            pass



test_cases = [  [2, 1, 5, 6, 2, 3],
                [3, 4, 1, 1, 1, 1, 1]
            ]