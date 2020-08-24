// Sum of Left Leaves
// Recursion yo

const TreeNode = require('./treeNode');

/**
 * Takes a TreeNode root and returns the sum of all of its left leaf values.
 *
 * @param {TreeNode} root
 * @return {Number}
 */
const sumOfLeftLeaves = root => {
    const util = (root, isLeft) => {
        // Make sure root is valid
        if (!root) {
            return 0;
        }
        // Check if root has children, and if it was flagged as a left child
        if (!root.left && !root.right && isLeft) {
            return root.val;
        }
        // Recurse on left and right children
        return util(root.left, true) + util(root.right, false);
    };

    return util(root, false);
};

// Driver Code 
let root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);
console.log(sumOfLeftLeaves(root));
