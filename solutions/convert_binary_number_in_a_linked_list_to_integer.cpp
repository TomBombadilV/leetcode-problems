// Convert Binary Number in a Linked List to Integer

#include <iostream>

#include "linkedlist.hpp"

int convert(ListNode* head) {
    ListNode* curr = head;
    int res = 0;
    
    while (curr != NULL) {
        int val = curr->val;
        res = res * 2 + val;
        curr = curr->next;
    }

    return res;
}

int main() {
    std::vector<std::vector<int>> cases = {
        {1, 0, 1, 0},
        {1},
        {0},
        {1,0,0,1,0,0,1,1,1,0,0,0,0,0,0},
        {0,0}
    };

    std::vector<int> expected = {
        10,
        1,
        0,
        18880,
        0
    };
   
    for (unsigned i = 0; i < cases.size(); i++) {
        ListNode* l = buildList(cases[i]);
        std::cout << convert(l) << " expected " << expected[i] << "\n";
    }
}
