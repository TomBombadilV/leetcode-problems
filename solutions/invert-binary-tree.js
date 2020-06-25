// Invert Binary Tree

function invertTree (root) {
    if (root) {
        const temp = root.left;
        root.left = root.right;
        root.right = temp;

        if (root.left) {
            invertTree(root.left);
        } 
        if (root.right) {
            invertTree(root.right);
        }
    }
    return root;
}

// Driver Code
const TreeNode = require('./tree-node.js')
const root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(7);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(9);

invertTree(root);
