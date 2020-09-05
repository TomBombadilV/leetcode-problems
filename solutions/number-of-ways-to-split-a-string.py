# Number of Ways to Split a String
# 1. There is only one way to split the ones, calculate that
# 2. Calculate number of 0s between each chunk, ignoring the 0s within a chunk.
#    The number of variances between two chunks is the number of 0s plus one
#    ex: 1001 can be split 1|001 10|01 100|1 
# 3. Multiply the variances between each set of chunks
# Time: O(n) | Space: O(1)

from test import test

def num_ways(s: str) -> int:
    ones = s.count('1')
    # If number of 1s not divisible by 3, or string is not at least 3 chars long,
    # there are 0 ways to split string
    if len(s) < 3 or ones % 3 != 0:
        return 0
    # If no 1s in the string, there are (n - 2) + (n - 3) + ... + 1 ways to split it
    # ex: 00000 => 0|0|000, 0|00|00, 0|000|0, 00|0|00, 00|00|0, 000|0|0
    if ones == 0:
        return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)
    # Number of 1s in each chunk
    ones /= 3
    curr_ones, curr_zeroes = 0, 0
    ways = 1
    # Find first 2 chunks and count number of 0s after each
    i = 0
    for _ in range(2):
        # Pass chunk of 1s (and 0s interspersed)
        while i < len(s) and curr_ones < ones: 
            if (s[i] == '1'):
                curr_ones += 1
            i += 1
        # Count 0s after chunk
        while i < len(s) and s[i] == '0':
            curr_zeroes += 1
            i += 1
        # Multiply ways
        ways *= curr_zeroes + 1
        # Reset count
        curr_ones, curr_zeroes = 0, 0
    return ways % (10 ** 9 + 7)
 
# Driver Code
cases = [["10101", 4], ["1001", 0], ["0000", 3], ["100100010100110", 12], 
         ["", 0], ["111", 1], ["1011", 2], ["00000000", 21]]
test(num_ways, cases)
