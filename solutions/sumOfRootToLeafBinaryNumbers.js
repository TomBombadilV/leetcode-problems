// Sum of Root to Leaf Binary Numbers

const test = require('./test');
const TreeNode = require('./treeNode');

/**
 * Recursively traverse tree, keeping track of sum by multiplying
 * current sum by 2 and adding the new digit (more space-efficient
 * than storing strings I believe)
 *
 * @param {TreeNode} root
 * @return {number}
 */
const sumRootToLeaf = root => {
    const recurse = (root, sum) => {
        if (!root) {
            return sum;
        }
        sum = sum * 2 + root.val;
        let res = 0;
        if (root.left) {
            res = recurse(root.left, sum);
        }
        if (root.right) {
            res += recurse(root.right, sum);
        }
        if (!root.left && !root.right) {
            console.log(res);
            res = sum;
        }
        return res;
    }

    return recurse(root, 0);
}; 

// Driver Code
let root = new TreeNode(1);
root.left = new TreeNode(0);
root.left.left = new TreeNode(0);
root.left.right = new TreeNode(1);
root.right = new TreeNode(1);
root.right.left = new TreeNode(0);
root.right.right = new TreeNode(1);
console.log(sumRootToLeaf(root));

root = new TreeNode(1);
root.right = new TreeNode(1);
root.right.left = new TreeNode(1);
root.right.right = new TreeNode(0);
console.log(sumRootToLeaf(root));

root = new TreeNode(0);
root.left = new TreeNode(1);
root.left.left = new TreeNode(0);
root.right = new TreeNode(0);
root.right.left = new TreeNode(0);
root.right.right = new TreeNode(0);
root.right.left.right = new TreeNode(1);
root.right.left.right.right = new TreeNode(1);
console.log(sumRootToLeaf(root));
