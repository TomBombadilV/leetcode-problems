# Kth Largest Element in an Array
# Use k variables to keep track of the k largest elements, updating while iterating through the Array
# Time: O(nlogn) | Space: O(k)

from math import log
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    if k > log(len(nums)):
        return sorted(nums)[-k]
    k_largest = []
    for n in nums:
        k_largest = place_in_sorted_array(k_largest, n, k) 
    return k_largest[-1]

def place_in_sorted_array(arr: List[int], n: int, k: int) -> None:
    # If n is larger than the smallest element in the array
    if len(arr) < k or n > arr[k-1]:
        curr = 0
        while curr < len(arr) and n < arr[curr]:
            curr += 1
        arr = arr[:curr] + [n] + arr[curr:k-1]
    return arr

test_cases = [  ([3, 2, 1, 5, 6, 3], 2),
                ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
                ([3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 8, 3, 1, 2, 10, 2, 4, 5, 5, 10, 6], 4)
            ]
for case in test_cases:
    nums, k = case
    print("{0}, k={1} => {2}".format(nums, k, findKthLargest(nums, k)))