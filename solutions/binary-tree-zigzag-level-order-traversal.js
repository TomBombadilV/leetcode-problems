// Binary Tree Zigzag Level Order Traversal
// Modified BFS with keeping track of levels and temporary array of current level
// nodes, reversed or not whenever level changes.

const TreeNode = require('./tree-node.js');

const zigzagLevelOrder = root => {
    if (!root) {
        return [];
    }

    // Queueueueueuuee
    let q = [[root, 0]];
    // Are we zigging or zagging
    let zig = true;
    let res = [];
    // Temporary space to put current level's node values
    let currArr = [];
    // Keep track of level to see if we are going to a new level
    let prevLevel = 0;
    
    // Basic BFS 
    while (q.length > 0) {
        let [curr, level] = q.shift();
       
        // If new level, add previous level values to result
        if (level != prevLevel) {
            res.push(zig ? currArr : currArr.reverse());
            zig = !zig;
            currArr = [];
        }

        // Add current val to array
        currArr.push(curr.val);
         
        // Add left and right nodes of current node
        if (curr.left) q.push([curr.left, level + 1]);
        if (curr.right) q.push([curr.right, level + 1]);
        
        // Update previous level
        prevLevel = level;
    }
    // Push array of last level
    res.push(zig ? currArr : currArr.reverse());
    return res;
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
