# Bag of Tokens
# Beats 90% submissions :D

from test import test
from typing import List

def bag_of_tokens_score(tokens: List[int], P: int) -> int:
    """ Takes a bag of tokens and returns the highest possible score.
        Do this by sorting the array, then flipping coins UP while power
        is high enough, then flipping coins DOWN while score is high enough
        until power is enough to flip up again.

        Time: O(n) | Space: O(1)
    """

    score = max_score = 0
    
    tokens.sort()

    while tokens:
        # If not enough power to flip up smallest token
        if P < tokens[0]:
            # And no score to flip down largest token
            if score < 1:
                # Give up
                return max_score
            # And have score to flip down largest token
            else:
                # Flip down largest token
                P += tokens.pop()
                score -= 1
        # If have enough power to flip up smallest token
        else:
            # Flip it up
            P -= tokens.pop(0)
            score += 1
            # Recalculate max score
            max_score = max(score, max_score)
    return max_score


# Driver Code
cases = [
    ([100], 50, 0),
    ([100], 100, 1),
    ([100, 200], 150, 1),
    ([100,200,300,400], 200, 2),
    ([], 10, 0),
    ([1,6,10,80,100,500], 1, 4)
]
#bag_of_tokens_score(cases[5][0], cases[5][1])
#test(bag_of_tokens_score, [cases[2]])
test(bag_of_tokens_score, cases)
