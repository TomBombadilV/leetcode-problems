// Binary Tree Zigzag Level Order Traversal

const TreeNode = require('./tree-node.js');

const zigzagLevelOrder = root => {
    if (!root) {
        return [];
    }
    let q = [[root, 0]];
    let zig = true;
    let res = [];
    let currArr = [];
    let prevLevel = 0;
    while (q.length > 0) {
        let [curr, level] = q.shift();
        
        if (level != prevLevel) {
            res.push(zig ? currArr : currArr.reverse());
            zig = !zig;
            currArr = [];
        }

        currArr.push(curr.val);
         
        if (curr.left) q.push([curr.left, level + 1]);
        if (curr.right) q.push([curr.right, level + 1]);
        
        prevLevel = level;
    }
    res.push(zig ? currArr : currArr.reverse());
    console.log(res);
};

// Driver Code
let root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);
zigzagLevelOrder(root);

root = null;
zigzagLevelOrder(root);

root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
zigzagLevelOrder(root);
