#ifndef TREE_NODE_HPP
#define TREE_NODE_HPP

struct TreeNode {
    int val;
    TreeNode* left = NULL;
    TreeNode* right = NULL;

    TreeNode(int n) : val(n) {}
};

#endif /* TREE_NODE_HPP */
