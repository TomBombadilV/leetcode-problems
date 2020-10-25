# Stone Game IV

import math
from test import test

def winner_square_game(n: int) -> bool:
    """ Calculates whether player A can win the game by taking the last set of stones.

        Use dp to calculate whether player A can win a game with 1 through n stones.
        If player A can select a set of stones from n that leaves a number m remaining,
        and we have shown that player A CANNOT win with m stones remaining, then player A
        can win with n.
    """
    res = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, math.floor(math.sqrt(i)) + 1):
            if not res[i - j * j]:
                res[i] = True
                break
    return res[-1]

# Driver Code
cases = [
    (1, True), (2, False), (4, True), (7, False), (17, False)
]
test(winner_square_game, cases)
