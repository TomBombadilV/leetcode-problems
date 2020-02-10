# Word Break
# 

from typing import Dict, List
from collections import defaultdict

def wordBreak(s: str, wordDict: List[str]) -> bool:
    memo = defaultdict(bool)
    for word in wordDict:
        memo[word] = True
    return recurse(s, memo)

def recurse(s: str, memo: Dict) -> bool:
    #print(s, memo)
    if s in memo and memo[s]:
        return True
    for i in range(len(s)):
        if s[i+1:] in memo:
            remaining_string_works = memo[s[i+1:]]
        else:
            remaining_string_works = wordBreak(s[i+1:], memo)
            memo[s[i+1:]] = remaining_string_works
        if s[:i+1] in memo and memo[s[:i+1]] and remaining_string_works:
            return True
    return False

test_cases = [  ("leetcode", ["leet", "code"]),
                ("applepenapple", ["apple", "pen"]),
                ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
                ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
]

for case in test_cases:
    s, wordDict = case
    print("{0}, {1} => {2}".format(s, wordDict, wordBreak(s, wordDict)))