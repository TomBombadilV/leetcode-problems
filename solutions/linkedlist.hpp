// List Node struct for building linked lists

#include <vector>

#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP

struct ListNode {
    int val;
    ListNode *next = NULL;

    ListNode(int v) {
        val = v;
    }
};

//template <typename T>
//ListNode buildList(std::vector<T> l);

ListNode *buildList(std::vector<int> l);
ListNode *buildRandomList(int n);
void printLinkedList(ListNode *head);

#endif /* LINKED_LIST_HPP */
