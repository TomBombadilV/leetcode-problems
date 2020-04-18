# Given two strings, where # means backspace, check whether they are equal when
# typed into empty text editors.

def backspaceCompare(S: str, T: str) -> bool:
    def typeString(s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i > 0:
                    s = s[:i - 1] + s[i + 1:]
                    i -= 1 
                else:
                    s = s[1:]
            else:
                i += 1
        return s
    return typeString(S) == typeString(T)

# Constant space - no string manipulation
def backspaceCompare(S: str, T: str) -> bool:
    """ Compare the strings backwards
    """
    i, j = len(S) - 1, len(T) - 1

    def get_valid_char_index(s: str, i: int) -> int:
        # Takes in a string and an index. Returns the index of the next
        # valid character (character that is not deleted)
        backspace_count = 0
        # Delete stuff
        while i >= 0 and (s[i] == '#' or backspace_count):
            if s[i] == '#':
                backspace_count += 1
            else:
                backspace_count -= 1
            i -= 1
        return i

    while i >= 0 or j >= 0:
        i = get_valid_char_index(S, i)
        j = get_valid_char_index(T, j)
        # Make sure characters are the same
        if not(S[i] == T[j]): return False
        # Go to the next character
        i, j = i - 1, j - 1
    return True if i == j else False

# Driver Code
cases = [   ('nzp#o#g', 'b#nzp#o#g', True), 
            ('bbbextm', 'bbb#extm', False),
            ('ab#c', 'ad#c', True),
            ('ab##', 'c#d#', True),
            ('a##c', '#a#c', True),
            ('a#c', 'b', False)
]
for case in cases:
    S, T, ans = case
    res = backspaceCompare(S, T)
    print("Pass" if res == ans else "{0}, {1} failed with {2} expected {3}".format(S, T, res, ans))
