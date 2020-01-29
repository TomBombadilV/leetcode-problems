# Zig Zag Conversion
# Append each character in the string to its corresponding row in an array, 
# going up and down the row numbers.
# Time: O(n) | Space: O(n)

def convert(self, s: str, numRows: int) -> str:
    # One row means no zig zagging
    if numRows==1:
        return s
    # Which direction we're incrementing the row number
    going_up = False
    curr_level = 0
    solution = [[] for _ in range(numRows)]
    for c in s:
        solution[curr_level].append(c)
        # If we've reached the upper or lower bound of levels, flip direction
        if curr_level==numRows-1 or curr_level==0:
            going_up = not(going_up)
        curr_level += 1 if going_up else -1
    solution = ''.join(str(c) for l in solution for c in l)
    return solution