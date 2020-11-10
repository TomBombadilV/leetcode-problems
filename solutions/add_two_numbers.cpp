#include <iostream>
#include <vector>

#include "linkedlist.hpp"

ListNode* padListHead(ListNode *l1, int padSize) {
    ListNode* head = l1;
    for (unsigned i = 0; i < padSize; i++) {
        head = appendToHead(head, 0);
    }
    return head;
}

int recurse(ListNode* l1, ListNode* l2, ListNode* res) {
    int sum;

    if (l1->next == NULL && l2->next == NULL) {
        sum = (l1->val + l2->val);
    }
    else {
        sum = (l1->val + l2->val + recurse(l1->next, l2->next, res));
    }
    ListNode* node = new ListNode(sum % 10);
    node->next = res->next;
    res->next = node;

    return sum / 10;
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int lenL1 = linkedListSize(l1);
    int lenL2 = linkedListSize(l2);

    if (lenL1 > lenL2) {
        l2 = padListHead(l2, lenL1 - lenL2);
    }
    if (lenL2 > lenL1) {
        l1 = padListHead(l1, lenL2 - lenL1);
    }

    ListNode* res = new ListNode(-1);

    int carry = recurse(l1, l2, res);

    if (carry) {
        ListNode* node = new ListNode(carry);
        node->next = res->next;
        res->next = node;
    }

    return res->next;
}

int main() {
    /*std::cout << "Print null list\n";
    printLinkedList(NULL);
    std::vector<int> l = {1, 3, 5, 7, 9, 11};

    std::cout << "Build vector list\n";
    ListNode *head = buildList(l);

    std::cout << "Print vector list\n";
    printLinkedList(head);

    std::cout << "Build random list\n";
    ListNode *randomHead = buildRandomList(10); 

    std::cout << "Print random list\n";
    printLinkedList(randomHead);

    std::cout << "Print size of random list\n";
    std::cout << linkedListSize(randomHead);*/

    ListNode* l1 = buildList({7, 2, 4, 3});
    ListNode* l2 = buildList({5, 6, 4});

    printLinkedList(l1);
    printLinkedList(l2);

    ListNode* res = addTwoNumbers(l1, l2);
    printLinkedList(res);

}
