# Course Schedule
# Check the graph for loops

from collections import defaultdict
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Adjacency list
    adj_list = [[] for _ in range(numCourses)]

    # Fill adjacency list
    for p in prerequisites:
        course, prereq = p[0], p[1]
        adj_list[course].append(prereq)
    
    # Visited list
    visited = [False] * numCourses 
    
    # Call DFS on each unvisited vertex
    for i in range(numCourses):
        # Recursion stack is stack of vertices visited during current DFS 
        # traversal, whereas visited is vertices visited during entire
        # traversal
        recursion_stack = [False] * numCourses
        # Call DFS on current vertex 
        if not(dfs_util(i, adj_list, visited, recursion_stack)):
            return False
    return True

def dfs_util(i: int, adj_list: List[List[int]], visited: List[bool], recursion_stack: List[bool]) -> bool:
    # If vertex has already been visited before
    if visited[i]:
        # If vertex is already in recursion stack, we have a cycle. If not, then vertex was visited in a previous instance of DFS and was found to not contain a cycle
        return False if recursion_stack[i] else True
    # Add current vertex to recursion stack
    recursion_stack[i] = True
    # Mark current vertex as visited
    visited[i] = True
    # Perform DFS on all adjacent vertices
    for v in adj_list[i]:
        if not(dfs_util(v, adj_list, visited, recursion_stack[:])):
            return False
    return True

# Driver code
test_cases = [  (2, [[1, 0]]),
                (2, [[1, 0], [0, 1]]),
                (3, []),
                (3, [[0, 1], [1, 2], [2, 0]]),
                (3, [[0, 1], [1, 2]])
            ]
for case in test_cases:
    numCourses, prereqs = case
    print("{0} => {1}".format(case, canFinish(numCourses, prereqs)))
