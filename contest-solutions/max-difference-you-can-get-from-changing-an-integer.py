# Max Difference You Can Get From Changing an Integer
# 1. Find max num:
#    Maximizing a number would mean flipping the highest order non-9 digit to 9.
#    Iterate through the array and select the first digit that is not 9. Then
#    iterate through rest of array and change all instances of that digit to 9.
# 2. Find min num:
#    Minimizing a number would mean flipping the highest order digit to 0.
#    Since number must be nonzero and cannot have any leading zeroes, first check
#    first digit. If it is 1, then we can't flip the highest order digit to 0 or
#    we'd have a leading zero. So, we flip the next number that isn't 1 and all 
#    of its instances to a 1. If first digit is NOT 1, we flip it and all its 
#    other instances to 1.
# 3. Finally, return difference between the two.
# Time: O(n) | Space: O(n)

def maxDiff(num: int) -> int:
    
    def find_max(num: int) -> int:
        """
        Returns highest number found by replacing all instances of a digit in given
        number.
        """
        s_num = str(num)
        for i in range(len(s_num)):
            # Look for s_num instance of non-9 digit and replace with 9
            if s_num[i] < '9':
                s_num = s_num.replace(s_num[i], '9')
                break
        return int(s_num)

    def find_min(num: int) -> int:
        """
        Returns smallest non-zero number with no leading zeroes found by replacing all
        instances of a digit in given number.
        """
        s_num = str(num)
        # If s_num digit is not 1, replace all instances with 1
        replace_with = '1' if not(s_num[0] == '1') else '0'
        for i in range(len(s_num)):
            # Look for s_num instance of number higher than comparator and replace
            if s_num[i] > '1':
                s_num = s_num.replace(s_num[i], replace_with)
                break
        return int(s_num) 

    max_num = find_max(num)
    min_num = find_min(num)
    return max_num - min_num

# Driver Code
cases = [(555, 888), (9, 8), (123456, 820000), (10000, 80000), (9288, 8700)]
for case in cases:
    num, expected = case
    res = maxDiff(num)
    print("Passed" if res == expected else "{0} failed with {1} expected {2}".\
          format(num, res, expected))
