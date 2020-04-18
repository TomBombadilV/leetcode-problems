# Validate Binary Search Tree
# Basically DFS, but passing along a min and max based on parent node

from treenode import TreeNode
from math import inf

def isValidBST(root: TreeNode) -> bool:
    if not(root):
        return True
    return recurse(root, -inf, inf)

def recurse(node: TreeNode, min: int, max: int) -> bool:
    if node.val <= min or node.val >= max:
        return False
    res = True
    # If going to the left, pass current node val as new min
    if node.left:
        res = res and recurse(node.left, min, node.val)
    # If going to the right, pass current node val as new max
    if node.right:
        res = res and recurse(node.right, node.val, max)
    return res

root = TreeNode(2)
curr = root
curr.left = TreeNode(1)
curr.right = TreeNode(3)
print(isValidBST(root))

root = TreeNode(5)
curr = root
curr.left = TreeNode(1)
curr.right = TreeNode(4)
curr = curr.right
curr.left = TreeNode(3)
curr.right = TreeNode(6)
print(isValidBST(root))

root = None
print(isValidBST(root))