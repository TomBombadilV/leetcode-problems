# 3Sum
# Sort list, have three pointers checking for zero sum triplets
# Time: O(n^2) | Space: O(1)

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Sort the list!
    nums = sorted(nums)
    solution = []
    # Since we're finding triples, iterate to the third to last item
    for i in range(len(nums)-2):
        # Since the list is sorted, if we're in positive numbers then we're not 
        # going to be able to negate this number back to 0 with the following 
        # positive numbers
        if nums[i] > 0:
            break
        # If we've already checked the same number, we don't want to add 
        # duplicates to our list
        if i > 0 and nums[i] == nums[i-1]:
            pass
        else:
            # Set pointers to the remaining numbers, one at the start and one 
            # at the end
            j, k = i+1, len(nums) - 1
            curr_sum = nums[i] + nums[j] + nums[k]
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                # If the sum is too small (less than 0), increase the small 
                # pointer
                if curr_sum < 0:
                    j+=1
                # If the sum is too big (more than 0), decrease the large 
                # pointer
                elif curr_sum > 0: 
                    k-=1
                # If the sum is correct, save the solution
                else:
                    solution.append([nums[i], nums[j], nums[k]])
                    # Ignore repeating numbers
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j > k and nums[k] == nums[k-1]:
                        k-=1
                    # Move pointers to next pair
                    j+=1
                    k-=1
    return solution