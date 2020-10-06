// Insert into a Binary Search Tree 

const test = require('./test');

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
const insertIntoBST = (root, val) => {
    if (!root) {
        return new TreeNode(val);
    }
    if (val < root.val) {
        if (root.left) {
            insertIntoBST(root.left, val);
        }
        else {
            root.left = new TreeNode(val);
        }
    }
    else {
        if (root.right) {
            insertIntoBST(root.right, val);
        }
        else {
            root.right = new TreeNode(val);
        }
    }
    return root;
};
