# Flatten Binary Tree to Linked List

from typing import List

"""def flatten(root: TreeNode) -> None:
    if root:
        l = inorder_traversal(root, [])
        root.left = None
        curr = root
        for i in range(1, len(l)):
            curr.right = TreeNode(l[i])
            curr = curr.right

def inorder_traversal(root: TreeNode, solution: List[int]):
    solution.append(root.val)
    if root.left:
        inorder_traversal(root.left, solution)
    if root.right:
        inorder_traversal(root.right, solution)
    return solution"""

def flatten(root: TreeNode) -> None:
    if root:
        if not(root.left) and not(root.right):
            return root
        if root.left and root.right:
            left_end = flatten(root.left)
            right_end = flatten(root.right)
            right = root.right
            root.right = root.left
            root.left = None
            left_end.right = right
            return right_end
        if root.left:
            left_end = flatten(root.left)
            root.right = root.left
            root.left = None
            return left_end
        if root.right:
            right_end = flatten(root.right)
            return right_end