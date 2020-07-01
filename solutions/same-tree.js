// Same Tree

const treeNode = require('./tree-node.js');

const isSameTree = function(p, q) {
    // If both p and q don't exist, stop traversing and return True
    if (!p && !q) {
        return true;
    }
    // If one of p or q doesn't exist, or their values aren't the same, return False
    if (!p || !q || p.val != q.val) {
        return false;
    }
    // Recurse on the left nodes and the right nodes
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

// Driver Code
// Case 1
let pRoot = new treeNode(1);
pRoot.left = new treeNode(2);
pRoot.right = new treeNode(3);

let qRoot = new treeNode(1);
qRoot.left = new treeNode(2);
qRoot.right = new treeNode(3);

console.log(isSameTree(pRoot, qRoot));

// Case 2
pRoot = new treeNode(1);
pRoot.left = new treeNode(2);

qRoot = new treeNode(1);
qRoot.right = new treeNode(2);

console.log(isSameTree(pRoot, qRoot));
