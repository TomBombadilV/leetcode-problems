# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree_DFS(l: List) -> TreeNode:
    if not(l):
        return None
        
    def build(root: TreeNode, l: List, i: int) -> TreeNode:
        root.left = TreeNode(l[i]) if i < len(l) and l[i] else None
        root.right = TreeNode(l[i + 1]) if i + 1 < len(l) and l[i + 1] else None
        i += 2
        i = build(root.left, l, i) if root.left else i
        i = build(root.right, l, i) if root.right else i
        return i

    root = TreeNode(l[0])
    build(root, l, 1)
    return root

def buildTree_BFS(l: List) -> TreeNode:
    if not(l):
        return None
    
    head = TreeNode(l[0])
    q = [head]
    i = 1
    while q:
        curr, q = q[0], q[1:]
        if i < len(l) and l[i]:
            curr.left = TreeNode(l[i])
            q.append(curr.left)
        i += 1
        if i < len(l) and l[i]:
            curr.right = TreeNode(l[i])
            q.append(curr.right)
        i += 1
    return head


# Prints entire tree
def print_tree(root) -> None:
    def print_tree_util(node: TreeNode, branch: str, child_branch: str) -> None:
        print(branch, node.val)
        if node.left and node.right:
            print_tree_util(node.left, child_branch + '├───', child_branch + '│    ')
        if node.left and not(node.right):
            print_tree_util(node.left, child_branch + '└───', child_branch + '     ')
        if node.right:
            print_tree_util(node.right, child_branch + '└───', child_branch + '     ')
    print_tree_util(root, '', '')

if __name__ == '__main__':
    l = [5, 3, 6, 2, 4, None, None, 1]
    root = buildTree_BFS(l)
    print_tree(root)

    l = [1, 10, 5, 1, 0, 6]
    root = buildTree_BFS(l)
    print_tree(root)
