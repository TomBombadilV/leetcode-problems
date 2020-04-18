def moveZeroes(self, nums: List[int]) -> None:
    # Mark boundary between nonzeroes and zeroes
    j = 0
    for i, n in enumerate(nums):
        # If not zero, move to boundary point
        if not(n == 0):
            # Make sure it's not already at the boundary point
            if not(i == j):
                nums[j] = n
                nums[i] = 0
            # Increment boundary point
            j+=1
            
