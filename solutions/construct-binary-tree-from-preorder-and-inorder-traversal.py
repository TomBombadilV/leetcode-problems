# Construct Binary Tree from Preorder and Inorder Traversal

from treenode import TreeNode
from typing import List

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    recurse()
    
def recurse(preorder: List[int], inorder: List[int]) -> TreeNode:
    stack = []
    while inorder[0] != preorder[0]:
        stack.append(inorder[0])
        inorder = inorder[1:]
    root = preorder[0]
    inorder, preorder = inorder[1:], preorder[1:]
    root.left = recurse(#left)
    root.right = recurse(#right)
    return root