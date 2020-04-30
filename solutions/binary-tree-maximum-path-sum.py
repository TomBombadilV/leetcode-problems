# Binary Tree Maximum Path Sum
# 

from math import inf
from treenode import TreeNode

def max_path_sum(root: TreeNode) -> int:
    if not(root.left) and not(root.right):
        return root.val, root.val
    if root.left and not(root.right):
        l_path, l_depth = max_path_sum(root.left)
        return max(l_path, root.val + l_depth, root.val), max(root.val, root.val + l_depth)
    if root.right and not(root.left):
        r_path, r_depth = max_path_sum(root.right)
        return max(r_path, root.val + r_depth, root.val), max(root.val, root.val + r_depth) 
    else:
        l_path, l_depth = max_path_sum(root.left)
        r_path, r_depth = max_path_sum(root.right)
        # Max depth is root plus left, plus right, or plus neither
        max_depth = max(l_depth, r_depth, 0) + root.val
        # Max path is left plus right plus root, left plus root, right plus root, left's
        # max path, right's max path, or just root
        max_path = max(l_depth + r_depth + root.val, 
                       l_depth + root.val,
                       r_depth + root.val,
                       l_path,
                       r_path,
                       root.val)
        return max_path, max_depth

def maxPathSum(root: TreeNode) -> int:
    return max_path_sum(root)[0]

# Driver Code

# Case 1
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root))

# Case 2
root = TreeNode(-3)
print(maxPathSum(root))

# Case 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(maxPathSum(root))

# Case 4
root = TreeNode(-2)
root.left = TreeNode(1)
print(maxPathSum(root))

# Case 5
root = TreeNode(2)
root.left = TreeNode(-1)
print(maxPathSum(root))
