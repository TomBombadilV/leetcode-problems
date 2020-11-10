#include <iostream>
#include <vector>

#include "linkedlist.hpp"

/* 
 * Adds given number of ListNodes with 0 value to the head of given list
 */
ListNode* padListHead(ListNode *l1, int padSize) {
    ListNode* head = l1;
    for (unsigned i = 0; i < padSize; i++) {
        head = appendToHead(head, 0);
    }
    return head;
}

/* 
 * Adds two linked lists together recursively
 */
int recurse(ListNode* l1, ListNode* l2, ListNode* res) {
    int sum;
    
    // If at the tail of both lists, sum will have no carry / no need to recurse
    if (l1->next == NULL && l2->next == NULL) {
        sum = (l1->val + l2->val);
    }
    // Else, get carry by recursing
    else {
        sum = (l1->val + l2->val + recurse(l1->next, l2->next, res));
    }

    // Create new node to add to result
    ListNode* node = new ListNode(sum % 10);
    
    // Add new node right after head, because placeholder head allows us to preserve 
    // list outside of this function's scope
    node->next = res->next;
    res->next = node;

    return sum / 10;
}

/* 
 * Pads lists so they are the same length, then calls function
 * that recursively adds them together.
 */
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    
    // Get size of two lists
    int lenL1 = linkedListSize(l1);
    int lenL2 = linkedListSize(l2);

    // Pad the shorter list so it matches the length of longer list
    if (lenL1 > lenL2) {
        l2 = padListHead(l2, lenL1 - lenL2);
    }
    if (lenL2 > lenL1) {
        l1 = padListHead(l1, lenL2 - lenL1);
    }

    // Create placeholder node for result list so we can pass and
    // modify it in recursive function
    ListNode* res = new ListNode(-1);

    // Recursively add two lists, get final carry value
    int carry = recurse(l1, l2, res);

    // If carry value, add it to the result list as well (again, after
    // the placeholder head)
    if (carry) {
        ListNode* node = new ListNode(carry);
        node->next = res->next;
        res->next = node;
    }
    
    // Return list minus placeholder head
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

    l1 = buildList({1,2,3,4,5});
    l2 = buildList({9,8,7});

    printLinkedList(l1);
    printLinkedList(l2);

    ListNode* res = addTwoNumbers(l1, l2);
    printLinkedList(res);

}
