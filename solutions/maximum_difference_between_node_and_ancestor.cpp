#include <iostream>
#include <vector>

#include "treenode.hpp"

/* 
 * Calculates max difference for a subtree
 */
void recurse(TreeNode* root, int min, int max, int &maxDiff) {
    
    if (root == NULL) {
        return;
    }
   
    // Update min and max values with current root
    min = std::min(min, root->val);
    max = std::max(max, root->val);

    // Update max calculated difference with new values
    maxDiff = std::max(maxDiff, max - min);
    
    // Pass ancestor's min and max values to its left subtree
    if (root->left != NULL) {
       recurse(root->left, min, max, maxDiff);
    }

    // Pass ancestor's min and max values to its right subtree
    if (root->right != NULL) {
        recurse(root->right, min, max, maxDiff);
    }
}

int maxAncestorDiff(TreeNode* root) {
    int min = INT_MAX;
    int max = INT_MIN;
    int maxDiff = 0;

    recurse(root, min, max, maxDiff);

    return maxDiff;
}

int main() {
    TreeNode* root = new TreeNode(8);
    root->left = new TreeNode(3);
    root->right = new TreeNode(10);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(6);
    root->right->right = new TreeNode(14);

    std::cout << maxAncestorDiff(root) << "\n";

    root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(0);
    root->right->right->left = new TreeNode(3);

    std::cout << maxAncestorDiff(root) << "\n";
}
