# Binary Tree Inorder Traversal
# Done recursively and iteratively

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
    stack = []
    stack.append(root)
    while stack:
        curr = stack[-1]
        if curr.left:
            stack.append(curr.left)
        else:
            solution.append(stack.pop().val)
            if curr.right:
                stack.append(curr.right)
    return solution