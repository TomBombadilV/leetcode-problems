# Longest Valid Parentheses
#
#

"""def longestValidParentheses(s: str) -> int:
    max_len, open_count, close_count, curr_count = 0, 0, 0, 0
    for c in s:
        if c == "(":
            open_count += 1
        else:
            close_count += 1
        curr_count += 1
        if close_count > open_count:
            open_count, close_count, curr_count = 0, 0, 0
        elif close_count == open_count:
            max_len = max(max_len, curr_count)
        else:
            max_len = max(max_len, close_count * 2)
    return max_len"""

def longestValidParentheses(s: str) -> int:
    stack, max_arr = [], [0] * (len(s) + 1)
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif stack:
            last = stack.pop()
            max_arr[i + 1] = max_arr[last] + (i - last + 1)
    return max(max_arr)


test_cases = ["(()", ")()())", "", "()(()"]
expected_solutions = [2, 4, 0, 2]

for i, case in enumerate(test_cases):
    solution = longestValidParentheses(case)
    if not(solution == expected_solutions[i]):
        print("{0} => {1} expected {2}".format(case, solution, expected_solutions[i]))
    else:
        print("Passed")