# Symmetric Tree

from treenode import TreeNode

def isSymmetric(root: TreeNode) -> bool:
    # If root is null or root has no children
    if not(root) or (not(root.left or root.right)):
        return True
    # If root doesn't have both children
    if not(root.left and root.right):
        return False
    return recurse(root.left, root.right)

def recurse(left: TreeNode, right: TreeNode) -> bool:
    # If left and right vals are not equal
    if not(left.val == right.val):
        return False
    # If left node left child or right node right child
    if left.left or right.right:
        # Both left node left child and right node right child exist
        if left.left and right.right:
            if not(recurse(left.left, right.right)):
                return False
        # If not a pair
        else:
            return False
    # If left node right child or right node left child
    if left.right or right.left: 
        # Both left node right child and right node left child exist
        if left.right and right.left:
            if not(recurse(left.right, right.left)):
                return False
        # If not a pair
        else: 
            return False
    return True

"""root = TreeNode(1)
print(isSymmetric(root))

root = TreeNode(1)
root.left = TreeNode(2)
print(isSymmetric(root))

root = TreeNode(1)
root.right = TreeNode(2)
print(isSymmetric(root))"""

root = TreeNode(2)
curr = root
curr.left = TreeNode(3)
curr.right = TreeNode(3)
right = curr.right
curr = curr.left
curr.left = TreeNode(4)
curr = right
curr.left = TreeNode(5)
curr.right = TreeNode(4)
print(isSymmetric(root))

"""root = TreeNode(3)
curr = root
curr.left = TreeNode(9)
curr.right = TreeNode(20)
curr = curr.right
curr.left = TreeNode(15)
curr.right = TreeNode(7)
print(isSymmetric(root))

root = None
print(isSymmetric(root))

root = TreeNode(1)
curr = root
curr.left = TreeNode(2)
curr.right = TreeNode(2)
right = curr.right
curr = curr.left
curr.left = TreeNode(3)
curr.right = TreeNode(4)
curr = right
curr.left = TreeNode(4)
curr.right = TreeNode(3)
print(isSymmetric(root))

root = TreeNode(1)
curr = root
curr.left = TreeNode(2)
curr.right = TreeNode(2)
right = curr.right
curr = curr.left
curr.right = TreeNode(3)
curr = right
curr.right = TreeNode(3)
print(isSymmetric(root))
"""