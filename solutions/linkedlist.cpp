#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

#include "linkedlist.hpp"

/*
 * Builds a linked list from a given vector. Returns pointer
 * to head of list.
 */
//template <typename T>
//ListNode buildList(std::vector<T> l) {
ListNode* buildList(std::vector<int> l) {
    if (l.size() < 1) {
        return NULL;
    }
   
    ListNode *head = new ListNode(l[0]);
    ListNode *curr = head;

    // Build linked list from vector
    for (unsigned i = 1; i < l.size(); i++) {
        ListNode *node = new ListNode(l[i]);
        curr->next = node; 
        curr = curr->next;
    }

    return head;
}

/*
 * Prints the elements of a vector.
 */
template <typename T>
void printList(std::vector<T> list) {
    for (unsigned i = 0; i < list.size(); i++) {
        std::cout << list[i] << " ";
    }
    std::cout << "\n";
}

/*
 * Generates a vector of size n with randomly shuffled
 * numbers 0, ..., n - 1
 */
std::vector<int> randomList(int n) {
    std::vector<int> list;

    // Build list of 0...n - 1
    for (unsigned i = 0; i < n; i++) {
        list.push_back(i);
    }

    // Initialize random number generator
    auto rng = std::default_random_engine {};

    // Shuffle list using random number generator
    std::shuffle(std::begin(list), std::end(list), rng); 

    return list;
}

/*
 * Generates a linked list of size n, with randomly shuffled
 * numbers 0...n - 1. Returns pointer to head of list.
 */
ListNode* buildRandomList(int n) {
    if (n < 1) {
        return NULL;
    }
    
    // Generate list of randomly shuffled numbers 0...n - 1
    std::vector<int> nums = randomList(n);

    //printList(nums);
    
    ListNode *head = new ListNode(nums[0]);
    ListNode *curr = head;

    // Build linked list out of vector
    for (unsigned i = 1; i < nums.size(); i++) {
        ListNode *node = new ListNode(nums[i]);
        curr->next = node;
        curr = curr->next;
    }
    return head;
}

/*
 * Appends new node of given value to the head of the list.
 */
ListNode* appendToHead(ListNode* head, int val) {
    ListNode* node = new ListNode(val);
    node->next = head;
    return node;
}

/* 
 * Prints out the node values of a linked list.
 */
void printLinkedList(ListNode *head) {
    ListNode *curr = head;
    
    while (curr != NULL) {
        std::cout << (*curr).val << " ";
        curr = (*curr).next;
    }
    std::cout << "\n";
}

/* 
 * Takes head of list and returns size of list.
 */
int linkedListSize(ListNode *head) {
    
    int size = 0;
    ListNode *curr = head;
    
    while (curr != NULL) {
        size++;
        curr = curr->next;
    }

    return size;
}
