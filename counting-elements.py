# Given an integer array, count how many elements in the list exist such that 
# x + 1 also exists in the array

# Eye roll

from collections import Counter
from typing import List

def countElements(arr: List[int]) -> int:
    dic = Counter(arr)
    count = 0
    for n in arr:
        if n + 1 in dic:
            count += 1
    return count

# Driver code
l = [1, 1, 2, 4, 5]
print(countElements(l))
