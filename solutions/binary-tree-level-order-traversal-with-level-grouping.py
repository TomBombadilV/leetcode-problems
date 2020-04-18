# Binary Tree Level Order Traversal with Level Grouping

from treenode import TreeNode
from typing import List

def levelOrder(root: TreeNode) -> List[List[int]]:
    # If no root
    if not(root):
        return []
    q = []
    level, curr_level = 0, 0
    curr = (root, level)
    res = [[]]
    while q or curr:
        # If the current level is the same as the node level, add the node to existing group in result
        level = curr[1]
        if level == curr_level:
            res[-1].append(curr[0].val)
        # If the level is different, add a new group to the result
        else:
            res.append([curr[0].val])
            curr_level = level
        # Add left and right nodes and their levels to the queue
        if curr[0].left:
            q.append((curr[0].left, level+1))
        if curr[0].right:
            q.append((curr[0].right, level+1))
        # Get the next node in the queue
        curr = q[0] if q else None
        q = q[1:]
    return res
        
root = TreeNode(1)
curr = root
curr.right = TreeNode(2)
curr = curr.right
curr.left = TreeNode(3)
"""root = TreeNode(3)
curr = root
curr.left = TreeNode(9)
curr.right = TreeNode(20)
curr = curr.right
curr.left = TreeNode(15)
curr.right = TreeNode(7)"""
print(levelOrder(None))