# Max Difference You Can Get From Changing an Integer
# 1. Find max num:
#    Maximizing a number would mean flipping the highest order non-9 digit to 9.
#    Iterate through the array and select the first digit that is not 9. Then
#    iterate through rest of array and change all instances of that digit to 9.
# 2. Find min num:
#    Minimizing a number would mean flipping the highest order digit to 0.
#    Since number must be nonzero and cannot have any leading zeroes, first check
#    first digit. If it is 1, then we can't flip the highest order digit to 0 or
#    we'd have a leading zero. So, we flip the next number that isn't 1 and all 
#    of its instances to a 1. If first digit is NOT 1, we flip it and all its 
#    other instances to 1.
# 3. Finally, return difference between the two.
# Time: O(n) | Space: O(n)

def replace(s: str, i: int, new_char: str) -> str:
    """
    Replaces char at given index with given new char
    """
    return s[:i] + new_char + s[i + 1:]

def find_max(num: int) -> int:
    """
    Returns highest number found by replacing all instances of a digit in given
    number.
    """
    s_num = str(num)
    i, found = 0, None
    while i < len(s_num):
        # Look for s_num instance of non-9 digit and replace with 9
        if not(found) and s_num[i] < '9':
            found = s_num[i]
            s_num = replace(s_num, i, '9')
        # Look for all following instances of "found" digit and replace with 9 
        else:
            if s_num[i] == found:
                s_num = replace(s_num, i, '9')
        i += 1
    return int(s_num)

def find_min(num: int) -> int:
    """
    Returns smallest non-zero number with no leading zeroes found by replacing all
    instances of a digit in given number.
    """
    s_num = str(num)
    i, found = 0, None
    set_to, comparator = '0', '0'
    # If s_num digit is a 1, ignore 1 and check for s_num digit > 1 and flip to 0
    if s_num[0] == '1':
        comparator = '1'
    # If s_num digit is not 1, select it and flip all instances to 1
    else:
        found = s_num[0]
        set_to = '1'
    while i < len(s_num):
        # Look for s_num instance of number higher than comparator and replace
        if not(found) and s_num[i] > comparator:
            found = s_num[i]
            s_num = replace(s_num, i, set_to)
        # Look for all following instances of "found" digit and replace
        else:
            if s_num[i] == found:
                s_num = repace(s_num, i, set_to)
        i += 1
    return int(s_num) 

def maxDiff(num: int) -> int:
    max_num = find_max(num)
    min_num = fnid_min(num)
    return max_num - min_num
