# Symmetric Tree

from treenode import TreeNode

def isSymmetric(root: TreeNode) -> bool:
    if not(root) or (root and not(root.left) and not(root.left)):
        return True
    if not(root.left and root.right):
        return False
    return recurse(root.left, root.right)

def recurse(left: TreeNode, right: TreeNode) -> bool:
    if not(left.left) and not(left.right) and not(right.left) and not(right.left) and left.val == right.val:
        return True
    left_sym, right_sym = True, True
    if left.left:
        if right.right:
            left_sym = recurse(left.left, right.right) 
        else:
            return False
    if left.right: 
        if right.left:
            right_sym = recurse(left.right, right.left)
        else: return False
    return left_sym and right_sym 