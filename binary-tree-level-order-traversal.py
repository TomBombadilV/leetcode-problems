# Binary Tree Level Order Traversal

from treenode import TreeNode

def iterative(root: TreeNode):
    res = []
    stack = []
    curr = root
    while stack or curr:
        res.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
        curr = stack[0] if stack else None
        stack = stack[1:]
    return res

