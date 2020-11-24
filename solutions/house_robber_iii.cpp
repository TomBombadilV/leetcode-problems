// House Robber III
#include <algorithm>
#include <iostream>
#include <vector>

#include "treenode.hpp"

std::vector<int> dfs(TreeNode* root) {
    if (root == NULL) {
        return {0, 0};
    }

    // Get max of left subtree including and excluding left/right child
    std::vector<int> left = dfs(root->left);
    std::vector<int> right = dfs(root->right);

    // Max including root will be max excluding children
    int with = root->val + left[1] + right[1];
    // Max excluding root will be max either including or excluding children
    int without = std::max(left[0], left[1]) + std::max(right[0], right[1]);

    // Max values including and excluding current node
    return {with, without};
}

int rob(TreeNode* root) {
    std::vector<int> res = dfs(root);
    return std::max(res[0], res[1]);
}

int main() {
    /*std::vector< > cases = {
    };

    std::vector< > expected = {
    };

    for (unsigned i = 0; i < cases.size(); i++) {
        _ res = _(cases[i]);

        if (res == expected[i]) {
            std::cout << "Passed\n";
        }
        else {
            std::cout << res << " expected " << expected[i] << "\n";
        }
    }*/

    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(3);
    root->right->right = new TreeNode(1);

    std::cout << rob(root);
}
