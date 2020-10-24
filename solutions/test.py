# General test function that takes in a function and arguments and checks 
# against expected value

from copy import deepcopy
from typing import List

def test(function, cases: List) -> None:
    """
    Runs given function with given arguments and checks against expected value.
    cases parameter MUST be in format (arg1, arg2, ...., expected)
    """
    for case in cases:
        args, expected = case[:-1], case[-1]
        # Save args for printing in case they are manipulated in function
        orig_args = deepcopy(args)
        res = function(*args)
        # Check result against expected value
        print("Passed" if res == expected else "{0} failed with {1} expected {2}".\
              format(orig_args, res, expected))
