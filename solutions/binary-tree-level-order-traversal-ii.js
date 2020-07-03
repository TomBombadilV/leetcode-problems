// Binary Tree Level Order Traversal II

const TreeNode = require('./tree-node.js')

const levelOrderBottom = root => {
    if (!root) {
        return [];
    }

    let queue = [[root, 1]];
    let res = [];
    let prev_level = 0;
    
    while (queue.length > 0) {
        let [curr, level] = queue.shift();
        
        if (level != prev_level) {
            res.push([curr.val]);
        } else {
            res[res.length - 1].push(curr.val);
        }

        prev_level = level;
        if (curr.left) {
            queue.push([curr.left, level + 1]);
        } 

        if (curr.right) {
            queue.push([curr.right, level + 1]);
        }
        
    }
    return res.reverse();
};

// Driver Code
let root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);

console.log(levelOrderBottom(root));

// Case 2
root.left.left = new TreeNode(10);
root.left.left.right = new TreeNode(11);

console.log(levelOrderBottom(root));

// Case 3
root = null;
console.log(levelOrderBottom(root));
