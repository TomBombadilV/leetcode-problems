# Construct Binary Search Tree from Preorder Traversal
# Method 1:
# Insert each node into BST
# Time: Worst Case - O(n^2), Average Case - O(nlogn), Best Case - O(n)
# Method 2:
# Using a stack, if current val is less than previous val, it is the left child.
# If larger than previous val, keep popping until you encounter a value that is
# larger. Then it will be the right child of the next value.
# Time: O(n)

# Typical BST insertion
def insert(root: TreeNode, n: int) -> TreeNode:
    # If no root, set as root
    if not(root):
        root = TreeNode(n)
        return root
    # Find the insertion point
    curr = root
    while curr:
        # Number is smaller than current node
        if n < curr.val:
            # Insert as left child
            if not(curr.left):
                curr.left = TreeNode(n)
                return root
            # Or else, move to left child
            else:
                curr = curr.left
        # Number is larger than current node
        elif n > curr.val:
            # Insert as right child
            if not(curr.right):
                curr.right = TreeNode(n)
                return root
            # Or else, move to right child
            else:
                curr = curr.right
        # Value already exists in tree
        else:
            return root

# Method 1
# Insert each number into the BST
def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    for i in range(1, len(preorder)):
        insert(root, preorder[i])
    return root

# Method 2
def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    s = [root]
    for i in range(1, len(preorder)):
        if preorder[i] < s.peek().val:
            s.peek().left = TreeNode(preorder[i])
            s.append(preorder[i])
        else:
            while s and preorder[i] > s.peek():
               curr = s.pop()
            curr.right = TreeNode(preorder[i])
            s.push(curr.right)
    return root                 

# Driver Code
preorder = [8, 5, 1, 7, 10, 12]
bstFromPreorder(preorder)
