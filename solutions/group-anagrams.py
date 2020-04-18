# Group Anagrams
# Using dictionary where the sorted string is the key, iterate through the list 
# and put each string in the dictionary
# Time: O(n * mlogm) | Space: O(n)

from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)
    for s in strs:
        dic[''.join(sorted(s))].append(s)
    return [dic[a] for a in dic]

test_cases = [["eat", "tea", "tan", "ate", "nat", "bat"]]
for case in test_cases:
    print("{0} => {1}".format(case, groupAnagrams(case)))