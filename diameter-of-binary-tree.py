# Diameter of Binary Tree
# Find longest path for left and right nodes and add them together

from treenode import TreeNode
from typing import Tuple

def diameterOfBinaryTree(root: TreeNode) -> int:
    def diam_util(root: TreeNode) -> Tuple[int, int]:
        # If no root, return max depth 0 and longest path 0
        if not(root):
            return 0, 0
        # Get the max depth and the longest path of the left node 
        left_depth, left_max = diam_util(root.left)
        # Get the max depth and the longest path of the right node
        right_depth, right_max = diam_util(root.right)
        # Max path for current node is max depth of left and right nodes plus
        # current node minus 1 because we're counting edges
        curr_max = left_depth + right_depth
        # Return max depth and longest path of current node
        return max(left_depth, right_depth) + 1, max(left_max, right_max, curr_max)

    return diam_util(root)[1]
    
# Driver Code
head = TreeNode(1)
curr = head
curr.left = TreeNode(2)
curr.right = TreeNode(3)
curr = curr.left
curr.left = TreeNode(4)
curr.right = TreeNode(5)

print(diameterOfBinaryTree(head))

# Try another tree
head = TreeNode(1)
curr = head
curr.left = TreeNode(2)
curr.right = TreeNode(3)
curr = curr.left
curr.left = TreeNode(4)
curr.right = TreeNode(5)
curr.left.left = TreeNode(6)
curr.left.left.left = TreeNode(7)
curr.right.right = TreeNode(8)
curr.right.right.right = TreeNode(9)

print(diameterOfBinaryTree(head))
