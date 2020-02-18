# Binary Tree Inorder Traversal
# Done recursively and iteratively
# Time: O(n) | Space: O(n)

from treenode import TreeNode
from typing import List

def recursiveInorderTraversal(root: TreeNode) -> List[int]:
    solution = []
    if not(root):
        return solution
    return recurse(root, solution)
    
def recurse(node: TreeNode, solution: List) -> List[int]:
    if node.left:
        recurse(node.left, solution)
    solution.append(node.val)
    if node.right:
        recurse(node.right, solution)
    return solution

def iterative_inorder_traversal(root: TreeNode) -> List[int]:
    solution = []
    stack = []
    curr = root
    # Keep traversing the tree through the left nodes
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        if stack:
            curr = stack.pop()
            solution.append(curr.val)
            curr = curr.right
    return solution

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
print(iterative_inorder_traversal(root))