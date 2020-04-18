# Valid Parentheses
# Push brackets onto stack. When an ending paranthesis is encountered, pop the 
# previous one and make sure it's a matching opening parenthesis
# Time: O(n) | Space: O(n)

def isValid(s: str) -> bool:
    l = []
    bracket_dic = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in bracket_dic:
            if not(l):
                return False
            prev = l[-1]
            if prev == bracket_dic[c]:
                l.pop()
            else: 
                return False
        else:
            l.append(c)
    return False if l else True

test_cases = ["()", "()[]\{\}", "(])", "([)])", "{[]}", "["]
for case in test_cases:
    print("{0} is {1}".format(case, "valid" if isValid(case) else "invalid"))