# Maximum Depth of Binary Tree
# DFS keeping track of max level

from treenode import TreeNode

def maxDepth(root: TreeNode) -> int:
    return recurse(root, 1, 1) if root else 0

def recurse(node: TreeNode, level: int, max_level: int) -> int:
    if not(node.left or node.right):
        max_level = max(max_level, level)
    if node.left:
        max_level = max(max_level, recurse(node.left, level + 1, max_level))
    if node.right:
        max_level = max(max_level, recurse(node.right, level + 1, max_level))
    return max_level

root = TreeNode(3)
curr = root
curr.left = TreeNode(9)
curr.right = TreeNode(20)
curr = curr.right
curr.left = TreeNode(15)
curr.right = TreeNode(7)
print(maxDepth(root))