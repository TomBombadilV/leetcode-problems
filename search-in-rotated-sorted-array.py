# Search in Rotated Sorted Array
# Perform binary search to find the rotation point O(logn). Re-form the array 
# in sorted order O(1), then perform binary search again to find the target 
# value
# Time: O(logn) | Space: O(1)

def search(nums: List[int], target: int) -> int:


test_cases = [  ([4, 5, 6, 7, 0, 1, 2], 0),
                ([4, 5, 6, 7, 0, 1, 2], 3)
            ]

for case in test_cases:
    print("Target: {0}, Nums: {1} => {2}".format(case[1], case[0], search(case[0], case[1])))