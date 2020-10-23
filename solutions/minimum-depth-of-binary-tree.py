# Minimum Depth of Binary Tree

from treenode import TreeNode

def min_depth(root: TreeNode):
    """ Calculates the minimum depth of a binary tree (the depth)
        of the minimum path from root to a leaf
    """
    
    def util(root: TreeNode, depth: int):
        """ Takes treenode and current depth, calculates depth of 
            left and right nodes, returns the smaller of the two
        """
        # Check root exists
        if not root:
            return depth
       
        # Get depth of children. If no children, return current depth.
        # If only one child, only recurse on that child
        if root.left and root.right:
            return min(util(root.left, depth + 1), util(root.right, depth + 1))
        else if root.left:
            return util(root.left, depth + 1)
        else if root.right:
            return util(root.right, depth + 1)
        else:
            return depth + 1
    
    return util(root, 0)
