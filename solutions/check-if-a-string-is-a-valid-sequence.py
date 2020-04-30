# Check If a String is a Valid Sequence from Root to Leaves Path in a Binary Tree
# Whew what title
# 

from treenode import TreeNode
from typing import List

def isValidSequence(root: TreeNode, arr: List[int]) -> bool: 
    
    def recurse(root: TreeNode, arr: List[int]) -> bool:
        if not(root) or not(arr) or not(root.val == arr[0]):
            return False
        if root.val == arr[0] and len(arr) == 1 and not(root.left) and not(root.right):
            return True
        return recurse(root.left, arr[1:]) or recurse(root.right, arr[1:])

    return recurse(root, arr)

# Driver Code
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(0)

cases = [[0, 1, 0, 1], [0, 0, 1], [0, 1, 1], [0]]
for case in cases:
    print(isValidSequence(root, case))
