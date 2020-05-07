# Cousins in Binary Tree
# Get parent and depth of each node and compare.

from treenode import TreeNode
from typing import Union

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    s = [(root, None, 0)]
    depth = 0
    depths, parents = [], []
    while s:
        curr, parent, depth = s[0]
        s = s[1:]
        if curr.val == x or curr.val == y:
            depths.append(depth)
            parents.append(parent)
        if len(depths) == 2:
            return depths[0] == depths[1] and not parents[0] == parents[1]
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
