// Construct Binary Tree from Inorder and Postorder Traversal
// Get root value from end of postorder list, find index of root value in inorder list,
// create left and right subtrees based on the partition by that index.

const TreeNode = require('./tree-node.js');

const buildTree = (inorder, postorder) => {
    if (inorder.length == 0 || inorder.length != postorder.length) {
        return null;
    }
    // Root value will be at the end of postorder list (because postorder is Left Right Root)
    let rootVal = postorder[postorder.length - 1];
    let root = new TreeNode(rootVal);
    
    // Find index of root value in inorder list
    let insortRootIndex = inorder.indexOf(rootVal);

    // Split inorder and postorder lists according to root index, build left and right subtrees
    root.left = buildTree(inorder.slice(0, insortRootIndex), 
        postorder.slice(0, insortRootIndex));
    root.right = buildTree(inorder.slice(insortRootIndex + 1), 
        postorder.slice(insortRootIndex, postorder.length - 1));

    return root;
};

// Driver Code
const inorder = [9,3,15,20,7];
const postorder = [9,15,7,20,3];

console.log(buildTree(inorder, postorder));
