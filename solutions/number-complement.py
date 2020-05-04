# Number Complement

from math import log
from test import test

def findComplement(num: int) -> int:
    """
    Use XOR. Example: 
    num : 1010
    ones: 1111
    XOR : 0101
    """
    # Find order of highest set bit
    l = int(log(num, 2)) + 1
    # Create number of all ones of same length
    ones = 2 ** l - 1 
    # XOR to flip bits
    return num ^ ones 

# Driver Code
cases = [(5, 2), (1, 0), (0, 1), (10, 5)]
test(findComplement, cases)
