// Sum Root to Leaf Numbers

const TreeNode = require('./tree-node.js')

const sumUtil = (root, pathSum) => {
    if (!root) {
        return pathSum;
    }
    let sum = 0;
    pathSum += root.val;
    if (root.left) {
        sum += sumUtil(root.left, pathSum);
    }
    if (root.right) {
        sum += sumUtil(root.right, pathSum);
    }
    if (!root.left && !root.right) {
        sum += Number(pathSum);
    }
    return sum; 
};

const sumNumbers = root => {
    return sumUtil(root, '');
};

// Test Case 1
let root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
console.log(sumNumbers(root));

// Test Case 2
root = new TreeNode(4);
root.left = new TreeNode(9);
root.right = new TreeNode(0);
root.left.left = new TreeNode(5);
root.left.right = new TreeNode(1);
console.log(sumNumbers(root));
