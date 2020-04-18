# Binary Tree Level Order Traversal

from treenode import TreeNode

def iterative(root: TreeNode) -> List[int]:
    res = []
    queue = []
    curr = root
    while queue or curr:
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        curr = queue[0] if queue else None
        queue = queue[1:]
    return res

def recursive(root: TreeNode) -> List[int]:
    pass

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
#print(recursive(root, []))
print(iterative(root))