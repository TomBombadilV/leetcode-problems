# Binary Tree Pre Order Traversal

from treenode import TreeNode
from typing import List

def recursive(root: TreeNode, res: List[int]):
    if not(root):
        return res
    res.append(root.val)
    recursive(root.left, res)
    recursive(root.right, res)
    return res

def iterative(root: TreeNode):
    curr = root
    res = []
    stack = []
    while stack or curr:
        if curr.right:
            stack.append(curr.right)
        res.append(curr.val)
        if curr.left:
            curr = curr.left
        elif stack:
            curr = stack.pop()
        else:
            curr = None
    return res

"""root = TreeNode(1)
curr = root
curr.left = TreeNode(2)
curr.right = TreeNode(3)
curr = curr.left
curr.left = TreeNode(4)
curr.right = TreeNode(5)"""
root = TreeNode(1)
curr = root
curr.right = TreeNode(2)
curr = curr.right
curr.left = TreeNode(3)
print(recursive(root, []))
print(iterative(root))