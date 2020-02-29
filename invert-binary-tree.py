# Invert Binary Tree
# Blah blah blah

from treenode import TreeNode

def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = root.right, root.left
        if root.left:
            invertTree(root.left)
        if root.right:
            invertTree(root.right)
    return root