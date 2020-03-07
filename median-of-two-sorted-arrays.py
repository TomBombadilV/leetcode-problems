# Median of Two Sorted Arrays

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    total_nums = len(nums1) + len(nums2)
    med_index = math.ceil(total_nums/2)-1
    ptr_a = ptr_b = 0
    med = None
    for _ in range(med_index):
        # If ptr_b is past the end of nums2 or ptr_a is not past the end and is smaller than nums2 at ptr_b
        if not(ptr_b < len(nums2)) or (ptr_a < len(nums1) and nums1[ptr_a] < nums2[ptr_b]):
            ptr_a+=1
        else:
            ptr_b+=1
    if not(ptr_b < len(nums2)) or (ptr_a < len(nums1) and nums1[ptr_a] < nums2[ptr_b]):
        med = nums1[ptr_a]
        ptr_a+=1
    else:
        med = nums2[ptr_b]
        ptr_b+=1
    if total_nums % 2 == 0:
        if not(ptr_b < len(nums2)) or (ptr_a < len(nums1) and nums1[ptr_a] < nums2[ptr_b]):
            med+=nums1[ptr_a]
        else:
            med+=nums2[ptr_b]
        med = med/2
    return med