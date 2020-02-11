# Course Schedule
# Check the graph for loops

from collections import defaultdict
from typing import List

class GraphVertex:
    edges = []
    value = None
    marked = False

    def __init__(self, value: int):
        self.value = value

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass

test_cases = [  (2, [[1, 0]]),
                (2, [[1, 0], [0, 1]])
            ]
for case in test_cases:
    numCourses, prereqs = case
    print("{0} => {1}".format(case, canFinish(numCourses, prereqs)))