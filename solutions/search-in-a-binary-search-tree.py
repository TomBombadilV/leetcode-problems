# Search for a given value in a BST

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not(root):
        return None
    if val < root.val:
        return searchBST(root.left, val)
    if val > root.val:
        return searchBST(root.right, val)
    # val == root.val
    else:
        return root
