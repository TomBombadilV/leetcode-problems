# K Closest Points to Origin

import bisect
from math import sqrt 
from typing import List

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    res = []
    count = 0
    for x, y in points:
        d = sqrt(x ** 2 + y ** 2)
        if count < K:
            bisect.insort(res, (d, x, y))
            count += 1
        else:
            if d < res[-1][0]:
                res.pop()
                bisect.insort(res, (d, x, y))
    res = [[point[1], point[2]] for point in res]
    return res

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(kClosest(points,k))
