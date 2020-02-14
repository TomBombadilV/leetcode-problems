# Binary Tree Inorder Traversal
# Done recursively and iteratively
# Time: O(n) | Space: O(n)

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    stack = [root]
    curr = root
    # Keep traversing the tree through the left nodes
    while stack and curr:
        while curr.left:
            curr = curr.left
            stack.append(curr)
        curr = stack.pop()
        solution.append(curr.val)
        if curr.right:
            stack.append(curr.right)
    return solution

root = TreeNode(1)
curr = root
curr.left = TreeNode(2)
curr.right = TreeNode(3)
curr = curr.left
curr.left = TreeNode(4)
curr.right = TreeNode(5)
print(iterative_inorder_traversal(root))