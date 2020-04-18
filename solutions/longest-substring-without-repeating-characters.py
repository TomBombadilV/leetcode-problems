# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s: str) -> int:
    char_dic = {}
    ptr1 = max_len = 0
    for ptr2, curr_char in enumerate(list(s)):
        # If character has been encountered before, update ptr_1 iff the last 
        # instance of this character is greater than the last time a character 
        # was repeated and updated (makes sure we're not going backwards)
        if curr_char in char_dic and char_dic[curr_char + 1] > ptr1:
            ptr1 = char_dic[curr_char] + 1
        # Add or update current index of character to dict
        char_dic[curr_char] = ptr2
        # Update max len if current max string is longer than max
        max_len = max(max_len, ptr2 - ptr1 + 1)
    return max_len

s = "abcaxyzlm"
s = str(input("Enter a string: "))
print(lengthOfLongestSubstring(s))