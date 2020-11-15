// Range Sum of BST
#include <iostream>
#include <stack>

#include "treenode.hpp"

/* 
 * Iteratively traverses tree using stack. Sums all nodes with 
 * value within range.
 */
int rangeSumIterative(TreeNode* root, int &low, int &high) {
    
    int sum = 0;
    
    std::stack<TreeNode*> s;
    
    if (root != NULL) {
        s.push(root);
    }

    while (!s.empty()) {
        // Access top element
        TreeNode* curr = s.top();
        s.pop();
       
        // Check if current node's value is within range
        if (curr->val >= low && curr->val <= high) {
            sum += curr->val;
        }        
        
        // Traverse tree with left and right children
        if (curr->right != NULL) {
            s.push(curr->right);    
        }
        if (curr->left != NULL) {
            s.push(curr->left);
        }
    }

    return sum;
}

void recurse(TreeNode* root, int &low, int &high, int& sum) {
    if (root == NULL) {
        return;
    }

    if (root->val >= low && root->val <= high) {
        sum += root->val;
    }

    recurse(root->left, low, high, sum);
    recurse(root->right, low, high, sum);
}

/*
 * Recursively traverses tree. Sums all nodes with value within
 * given range.
 */
int rangeSumRecursive(TreeNode* root, int &low, int &high) {
    int sum = 0;
    recurse(root, low, high, sum);
    return sum;
}
    
int main() {
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(7);
    root->right = new TreeNode(15);
    root->right->right = new TreeNode(18);

    int low = 7;
    int high = 15;

    std::cout << rangeSumIterative(root, low, high) << "\n";
    std::cout << rangeSumRecursive(root, low, high) << "\n";
}
