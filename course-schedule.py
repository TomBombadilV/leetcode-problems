# Course Schedule
# Check the graph for loops

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Adjacency list
    a = [[] for _ in range(numCourses)]
    # Visited list
    v = [False] * numCourses
    for p in prerequisites:
        course, prereq = p[0], p[1]
        a[course].append(prereq)
    for i in range(numCourses):
        v[i] = True
        adjacency_list = a[i]
        if adjacency_list:
            i = 0
            curr = adjacency_list[i]
            while v[curr] == True:
                if i < len(adjacency_list):
                    i+=1
                    curr = adjacency_list[i]
            


test_cases = [  (2, [[1, 0]]),
                (2, [[1, 0], [0, 1]])
            ]
for case in test_cases:
    numCourses, prereqs = case
    print("{0} => {1}".format(case, canFinish(numCourses, prereqs)))