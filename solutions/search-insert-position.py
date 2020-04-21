# Search Insert Position
# Binary Search
# Time: O(logn) | Space: O(1)

def binary_search(nums: List[int], target: int) -> int:
    while start < end:
        start, end, mid = (start - end) // 2
         

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1 
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            

