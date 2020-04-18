# Merge Two Binary Trees

from treenode import TreeNode

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        new = TreeNode(t1.val + t2.val)
        new.left = mergeTrees(t1.left, t2.left)
        new.right = mergeTrees(t1.right, t2.right)
    elif t1 or t2:
        new = t1 if t1 else t2
    else:
        return None
    return new