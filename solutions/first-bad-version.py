# First Bad Version
# Method 1:
# Modified binary search using a dictionary to avoid repeated calls to API. 
# Check mid and left of mid to see if mid is first bad version.
# Time: O(logn) | Space: O(n)
#
# Method 2:
# Modified binary search. Check if mid is bad version. If not, look on the right.
# If so, look on the left. Stop when left and right cross. If firstBadVersion 
# was mid and we move to the left, the pointers will eventually cross and left 
# will end up pointing at that mid.
# Time: O(logn) | Space: O(1)

def isBadVersion(n: int) -> bool:
    """ 
    Determine whether given n is or comes after a bad version
    """
    # Hard coded at 4
    bad = 4
    return True if n >= bad else False

def firstBadVersion(n: int) -> int:
    """
    Method 1
    """
    # Log isBadVersion results to minimize calls to API
    dic = {}
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2

        # Update dic with new calls 
        if not(mid in dic):
            dic[mid] = isBadVersion(mid)
        if not(mid - 1 in dic):
            dic[mid - 1] = isBadVersion(mid - 1)
        
        # Binary search, checking if mid is first bad version
        if dic[mid] and not(dic[mid - 1]):
            return mid
        elif dic[mid]:
            right = mid - 1
        else:
            left = mid + 1
    # If never found, return -1
    return -1

def firstBadVersion(n: int) -> int:
    """
    Method 2
    """
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

cases = [i for i in range(10)]
for case in cases:
    print(firstBadVersion(case))
