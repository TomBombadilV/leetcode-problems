# Zig Zag Conversion
# Visit the locations of each row's letters in succession
# Time: O(n) | Space: O(n)

def convert(s: str, numRows: int) -> str:
    # One row means no zig zagging
    if numRows == 1:
        return s
    solution = ''
    s_len = len(s)
    for row in range(numRows):
        # The two increment values to find the row's indices
        inc_1 = 2*(numRows-1) if row==numRows-1 else 2*(numRows-1) - (2*row)
        inc_2 = inc_1 if (row==0 or row==numRows-1) else 2*(numRows-1) - inc_1 
        # bool to tell which increment value to use
        first_inc = True 
        curr_idx = row
        # Increment until you've reached the end of the string
        while curr_idx < s_len:
            solution += s[curr_idx]
            curr_idx += inc_1 if first_inc else inc_2
            first_inc = not(first_inc)
    return solution