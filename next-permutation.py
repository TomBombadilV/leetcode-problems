# Next Permutation
# Traverse the list from back to front, searching for the first instance where 
# the right number is larger than the left. Swap left number with the next 
# largest number to the right when found, and make the rest of the numbers to 
# the right from decreasing to inreasing. If never found, reverse list
# Time: O(n) | Space: O(n)

from typing import List
import sys

def find_next_swap_order(nums: List[int]) -> List[int]:
    # Swap the leftmost number with the next largest number in the list. Then 
    # order the rest of the list in ascending order
    target = nums[0]
    ans, idx = sys.maxsize, None
    # Find the next largest number in the list
    for i, n in enumerate(nums):
        if n > target and n <= ans:
            ans, idx = n, i
    # Swap the original number and its next largest number
    nums[idx] = target
    nums[0] = ans
    # Flip the rest of the list from descending to ascending order
    nums[1:] = list(reversed(nums[1:]))
    return nums

def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    # If length of list is 0 or 1, nothing happens
    if n < 2:
        return
    # Starting at the end of the list, find the first instance where the left 
    # number is smaller than the right
    left, right = n-2, n-1
    while nums[right] <= nums[left]:
        left-=1
        right-=1
        # If we reach the beginning of the list, then the list is in descending 
        # order. Return it in ascending order
        if left < 0:
            nums[0:] = list(reversed(nums))[0:]
            return
    nums[left:] = find_next_swap_order(nums[left:])

test_cases = [  [], 
                [1], 
                [1, 2], 
                [2, 1], 
                [2, 3, 1, 3, 3], 
                [1, 2, 5, 6, 4, 3, 2, 1], 
                [1, 2, 3], 
                [3, 2, 1, 4], 
                [3, 2, 1], 
                [1, 1, 5]
            ]
expected_solutions = [  [], 
                        [1], 
                        [2, 1], 
                        [1, 2], 
                        [2, 3, 3, 1, 3], 
                        [1, 2, 6, 1, 2, 3, 4, 5], 
                        [1, 3, 2], 
                        [3, 2, 4, 1], 
                        [1, 2, 3], 
                        [1, 5, 1]
                    ]
                    
for i, case in enumerate(test_cases):
    print("{0} -> ".format(case), end="")
    nextPermutation(case)
    print(case, case==expected_solutions[i])