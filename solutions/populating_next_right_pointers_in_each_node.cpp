#include <iostream>
#include <queue>
#include <vector>

#include "treenode.hpp"

void populate(TreeNode* root) {

    // Queue woot woot
    std::queue<std::pair<TreeNode*, int>> q;
    
    // Add root and its level to queue
    if (root != NULL) {
        std::pair<TreeNode*, int> curr(root, 0);
        q.push(curr);
    }

    while (!q.empty()) {
        // Get current TreeNode and level from queue
        std::pair<TreeNode*, int> curr = q.front();
        q.pop();
        TreeNode* currNode = curr.first;
        int currLevel = curr.second;
        
        // Push its children onto the queue
        if (currNode->left != NULL) {
            q.push(std::make_pair(currNode->left, currLevel + 1));
        }
        if (currNode->right != NULL) {
            q.push(std::make_pair(currNode->right, currLevel + 1));
        }

        // If there is a node after curr and that node is on the same level,
        // set it as curr's next
        if (!q.empty() && q.front().second == currLevel) {
            currNode->next = q.front().first;         
        }
    }
}

int main() {
    // Don't feel like adding a next attribute to my tree...
    /*TreeNode* root = new TreeNode(0);
    root->left = new TreeNode(1);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(6);

    populate(root);

    std::cout << root->next << " " << root->left->next << " " << root->right->next;*/
}
