# Maximum depth of a binary tree

def maxDepth(root: TreeNode) -> int:
    if not(root):
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

