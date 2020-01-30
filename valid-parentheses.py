# Valid Parentheses
# Push brackets onto stack. When an ending paranthesis is encountered, pop the 
# previous one and make sure it's a matching opening parenthesis
# Time: O(n) | Space: O(n)

def isValid(s: str) -> bool:
    l = []
    open_brackets, close_brackets = ["(", "{", "["], [")", "}", "]"]
    for c in s:
        if c in open_brackets:
            l.append(c)
        else:
            if not(l):
                return False
            prev = l[-1]
            if open_brackets.index(prev) == close_brackets.index(c):
                l.pop()
            else: 
                return False
    if l:
        return False
    return True

test_cases = ["()", "()[]\{\}", "(])", "([)])", "{[]}", "["]
for case in test_cases:
    print("{0} is {1}".format(case, "valid" if isValid(case) else "invalid"))