# Cousins in Binary Tree
# Perform BFS and stop when both nodes have been found.
# Time: O(n) | Space: O(n)

from treenode import TreeNode
from typing import Union

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    # Add root, its parent, and its depth to queue
    s = [(root, None, 0)]
    
    # Keep track of x and y's depths and parents
    depths, parents = [], []
    
    # Modified BFS
    while s:
        # Dequeue next node
        curr, parent, depth = s[0]
        s = s[1:]
    
        # If one node has already been found and current depth doesn't match
        if depths and not depth == depths[0]:
            return False

        # If node is x or y, save its depth and parent
        if curr.val == x or curr.val == y:
            depths.append(depth)
            parents.append(parent)

        # If both nodes have been found, check if they're cousins
        if len(depths) == 2:
            return depths[0] == depths[1] and not parents[0] == parents[1]
        
        # Continue BFS (append left and right children to queue)
        if curr.left:
            s.append((curr.left, curr, depth + 1))
        if curr.right:
            s.append((curr.right, curr, depth + 1))
    return False    


# Driver Code
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(4)
print(isCousins(root, 3, 4))
print(isCousins(root, 0, 1))
