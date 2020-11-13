#include <iostream>
#include "linkedlist.hpp"

/* 
 * Inserts a node into a sorted linked list
 */
ListNode* findInsertionPoint(ListNode* sortedHead, ListNode* sortedTail, ListNode *insert) {
    ListNode* curr = sortedHead;
    
    // Find the node BEFORE the point where node should be inserted.
    while (curr->next != NULL && curr != sortedTail && insert->val > curr->next->val) {
        curr = curr->next;
    }
    
    // Insert the node
    insert->next = curr->next;
    curr->next = insert;

    // If inserted after sortedTail, update sortedTail to point to insert
    if (curr == sortedTail) {
        sortedTail = insert;
    }
    
    return sortedTail;
}


ListNode* insertionSortList(ListNode* head) {
    
    // Keep track of sorted area
    ListNode* sortedTail = head;

    // Insert dummy node at head
    ListNode* node = new ListNode(-1);
    node->next = head;
    head = node;
  
    // While portion of list is unsorted
    while (sortedTail != NULL && sortedTail->next != NULL) {
        // Remove first node in unsorted section
        ListNode* curr = sortedTail->next;
        sortedTail->next = curr->next;
        // Insert into sorted section
        sortedTail = findInsertionPoint(head, sortedTail, curr);
    }

    // Remove dummy node
    return head->next;
}

int main() {
    ListNode* head = buildRandomList(0);
    printLinkedList(head);
    printLinkedList(insertionSortList(head));

    head = buildList({3,2,4});
    printLinkedList(head);
    printLinkedList(insertionSortList(head));
}
