# Summary Ranges

from test import test
from typing import List

def summary_ranges(nums: List[int]) -> List[str]:
    """ Condenses a sorted array of numbers into intervals.
        Time: O(n) | Space: O(n)
    """
    res = []
    
    if not nums:
        return res
    
    # Preserve current start of interval
    curr_start = nums[0]

    # Iterate through array from second index past end of array
    for i in range(1, len(nums) + 1):

        # If number is not an increment of previous number OR if past end of array,
        # then we need to close off the previous interval and start a new one
        if i == len(nums) or nums[i] != nums[i - 1] + 1:
            
            # If interval span is just one number then format is "0"
            if nums[i - 1] == curr_start:
                res.append(str(curr_start))
            # If interval span is multiple numbers, then format is "0->1"
            else:
                res.append("{0}->{1}".format(curr_start, nums[i - 1]))
            # Start new interval if we are not past the end of the array
            curr_start = nums[i] if i < len(nums) else None

    return res

# Driver Code
cases = [
    ([0,1,2,4,5,7], ["0->2","4->5","7"]),
    ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]), 
    ([], []),
    ([-1], ["-1"]),
    ([0], ["0"])
]
#test(summary_ranges, [cases[0]])
test(summary_ranges, cases)
