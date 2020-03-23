# Lowest Common Ancestor of a Binary Tree
# Using DFS, keep a stack of the nodes in the current path
#

from treenode import TreeNode

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    path, path_p, path_q = [], [], []
    stack = []
    curr = root
    while curr or stack:
        # Stop traversing if both nodes already found
        if path_p and path_q:
            break
        path.append(curr)
        if curr.right:
            stack.append((curr.right, path[:]))
        if curr == p:
            path_p = path[:]
        if curr == q:
            path_q = path[:]
        if curr.left:
            stack.append((curr.left, path[:]))
        if stack:
            curr, path = stack.pop()
        else:
            curr, path = None, None
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        res = path_p[i]
        i += 1
    return res

def alt_lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    stack = []
    curr = root
    parent_dic =  {}
    p_found, q_found = False, False
    while curr:
        if p_found and q_found:
            break
        if curr.right:
            parent_dic[curr.right] = curr
            stack.append(curr.right)
        if curr == p:
            p_found = True
        if curr == q:
            q_found = True
        if curr.left:
            parent_dic[curr.left] = curr
            stack.append(curr.left)
        curr = stack.pop() if stack else None
    p_path, q_path = [], []
    while not(p == root):
        p = parent_dic[p]
        p_path.append(p)
    while not(q == root):
        q = parent_dic[q]
        q_path.append(q)
    p_path = list(reversed(p_path))
    q_path = list(reversed(q_path))
    i, res = 0, root
    while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
        res = p_path[i]
        i += 1
    return res
    


"""root = TreeNode(1)
curr = root
curr.left = TreeNode(2)
curr.right = TreeNode(3)
curr = curr.left
p = curr
curr.left = TreeNode(4)
curr = curr.left
curr.right = TreeNode(6)
q = curr.right"""

root = TreeNode(3)
curr = root
curr.left = TreeNode(5)
curr = root.left
p = curr
curr.left = TreeNode(6)
curr.right = TreeNode(2)
curr = curr.right
curr.left = TreeNode(7)
curr.right = TreeNode(4)
q = curr.right
curr = root
curr.right = TreeNode(1)
curr = curr.right
curr.left = TreeNode(0)
curr.right = TreeNode(8)

"""root = TreeNode(1)
p = root
root.left = TreeNode(2)
q = root.left"""
print(alt_lowestCommonAncestor(root, p, q).val)