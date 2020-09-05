// All Elements in Two Binary Search Trees

const TreeNode = require('./treeNode');

/**
 * Perform in-order traversal of both trees. Append the resulting lists together,
 * then sort them.
 *
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
const getAllElements = (root1, root2) => {
    // In order traversal of BST
    const bstToList = (root, list) => {
        if (!root) {
           return; 
        }
        if (root.left) {
            bstToList(root.left, list);
        }
        list.push(root.val);
        if(root.right) {
            bstToList(root.right, list);
        }
    };
    // Convert bsts to lists
    let [l1, l2] = [[], []];
    bstToList(root1, l1);
    bstToList(root2, l2);
    // Concatenate lists and sort them
    return l1.concat(l2).sort((a, b) => {return a <= b ? -1 : 0});
};

// Driver Code
//let root1 = new TreeNode(2);
//root1.left = new TreeNode(1);
//root1.right = new TreeNode(4);
let root1 = null;

let root2 = new TreeNode(1);
root2.left = new TreeNode(0);
root2.right = new TreeNode(3);

console.log(getAllElements(root1, root2));
