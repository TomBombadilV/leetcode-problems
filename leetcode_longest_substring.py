# LeetCode Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    char_dic = {}
    ptr1 = max_len = 0
    for ptr2, curr_char in enumerate(list(s)):
        if curr_char in char_dic:
            ptr1 = max(ptr1, char_dic[curr_char]+1)
            char_dic[curr_char] = ptr2
            max_len = max(max_len, ptr2 - ptr1 + 1)
        else:
            char_dic[curr_char] = ptr2
            max_len = max(max_len, ptr2 - ptr1 + 1)
    return max_len

s = "abcaxyzlm"
print(lengthOfLongestSubstring(s))