# Product of Array Except Self
# Method 1: 
# Create two arrays - one that stores the product of all numbers before, and one
# that stores the product of all numbers after. The product of all numbers 
# except self will be the product of those two arrays.
# Time: O(n) | Space: O(n)
# Method 2:
# Create one single result array and perform both operations on that array.
# Time: O(n) | Space: O(n)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    prod_a, prod_b = [1] * len(nums), [1] * len(nums)
    # Array of product of all numbers before
    for i in range(len(nums) - 1):
        prod_a[i + 1] = prod_a[i] * nums[i]
    # Array of product of all numbers after
    for i in reversed(range(1, len(nums))):
        prod_b[i - 1] = prod_b[i] * nums[i]
    # Return product of two arrays
    return [prod_a[i] * prod_b[i] for i in range(len(nums))]

def productExceptSelf

# Driver code
l = [1, 2, 3, 4]
print(productExceptSelf(l))

