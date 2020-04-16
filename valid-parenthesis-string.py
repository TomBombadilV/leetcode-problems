# Valid Parenthesis String
# Keep track of window of possible left parentheses values and check against all
# encountered right parentheses
# Time: O(n) | Space: O(1)

def checkValidString(s: str) -> bool:
    # Keep track of minimum and maximum amount of possible left parentheses
    left_min, left_max = 0, 0
    for c in s:
        # If (, increase window of possible amounts
        if c == '(':
            left_min += 1
            left_max += 1
        # If ), decrease window of possible amounts
        elif c == ')':
            left_min = max(left_min - 1, 0)
            left_max -= 1 
        # If *, widen window of possible amounts
        else:
            left_min = max(left_min - 1, 0)
            left_max += 1
        # If maximum possible left parentheses is less than 0, then string is invalid
        if left_max < 0:
            return False
    # Make sure no left parentheses are left
    return left_min == 0
    
# Driver code
cases = ['()', '(*)', '(*))', '(*)))', '((()())*))', '(', ')', '(*()']
for case in cases:
    print(checkValidString(case))
