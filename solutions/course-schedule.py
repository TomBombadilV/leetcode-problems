# Course Schedule
# Check the graph for cycles using a variation of topological sort via DFS
# Time: O(V + E) | Space: O(V + E)

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Adjacency list
    adj_list = [[] for _ in range(numCourses)]

    # Fill adjacency list
    for p in prerequisites:
        course, prereq = p[0], p[1]
        adj_list[course].append(prereq)
    
    # Visited list
    visited = [0] * numCourses 
    
    # Call DFS on each unvisited vertex
    for i in range(numCourses):
        # Call DFS on current vertex 
        if not(dfs(i, adj_list, visited)):
            return False
    return True

def dfs(i: int, adj_list: List[List[int]], visited: List[int]) -> bool:
    # If vertex has already been visited during this DFS, meaning a cycle exists
    if visited[i] == -1:
        return False 
    # Vertex was visited in another DFS and found not to have a cycle
    if visited[i] == 1:
        return True
    # Mark current vertex as visited during current DFS
    visited[i] = -1
    # Perform DFS on all adjacent vertices
    for v in adj_list[i]:
        if not(dfs(v, adj_list, visited)):
            return False
    # Vertex is determined to not have any cycles
    visited[i] = 1
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
