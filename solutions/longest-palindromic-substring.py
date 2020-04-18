# Longest Palindromic Substring
# Using each char in the string (and the spaces betwen characters) as potential 
# "centers" for a palindrome, check each potential for the longest surrounding 
# palindrome
# Time: O(n^2) | Space: O(n)

def longestPalindrome(s: str) -> str:
    max_pal, max_len = '', 0
    for i in range(2 * len(s) - 1):
        # Get longest surrounding palindrome for current index
        curr_max, curr_max_len = get_longest_surrounding_pal(i, s)
        # Update max
        if curr_max_len > max_len:
            max_pal = curr_max
            max_len = curr_max_len
    return max_pal

def get_longest_surrounding_pal(i:int, s:str) -> (str, int):
    # Get indices to the immediate left and right of current index
    # If we're checking a char
    if i % 2 == 0:
        ptr_a, ptr_b = int(i/2 - 1), int(i/2 + 1)
        # Add char to current palindrome string
        curr_max, curr_max_len = s[int(i/2)], 1
    # If we're checking a space between chars
    else:
        ptr_a, ptr_b = i//2, i//2 + 1
        # Add null to current palindrome string
        curr_max, curr_max_len = '', 0
    # While we havent reached past the beginning or end of the string and both 
    # the left and right chars are equal, increment pointers
    while ptr_a >= 0 and ptr_b < len(s) and s[ptr_a]==s[ptr_b]:
        curr_max = s[ptr_a] + curr_max + s[ptr_b]
        curr_max_len += 2
        ptr_a -= 1
        ptr_b += 1
    return curr_max, curr_max_len

s = str(input("Enter a string: "))
print(longestPalindrome(s))