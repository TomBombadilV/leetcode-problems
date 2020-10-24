# Asteroid Collision

from test import test
from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    """ Takes a list of asteroids, collides them, returns remaining
        asteroids.
    """
    res = []
    
    for i, asteroid in enumerate(asteroids):
        # Add all asteroids moving to the right to res
        if asteroid > 0:
            res.append(asteroid)
        # If asteroid is moving to the left
        elif asteroid < 0:
            # Remove all prior asteroids that are moving to the right and smaller
            while res and res[-1] > 0 and res[-1] < abs(asteroid):
                res.pop()
            
            # If no asteroids left, or prior asteroid is also moving left, add asteroid
            if not res or res[-1] < 0:
                res.append(asteroid)
            # If prior asteroid is bigger, don't add current asteroid (it explodes)
            elif res[-1] > abs(asteroid):
                pass
            # If prior asteroid size is same as current, it explodes
            elif res[-1] == abs(asteroid):
                res.pop()
            # Should never happen 
            else:
                pass
        # 0 asteroid wouldn't exist
        else:
            pass
    return res

# Driver Code
cases = [
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ([10, 2, -5, -1], [10]),
    ([8,-8], [])
]
test(asteroidCollision, cases)
