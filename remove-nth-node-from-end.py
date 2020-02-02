# Remove Nth Node From End of List
# Have two pointers n distance apart. When second pointer reaches end of list, 
# first pointer will be n from end
# Time: O(n) | Space: O(1)

from typing import List
from listnode import *

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head:
        # Have both pointers start at the head
        ptr_a, ptr_b = head, head
        # Move the second pointer n spaces away from the head
        for i in range(n):
            ptr_b = ptr_b.next
        if ptr_b:
            # Move both pointers until ptr_b is at the end of the list
            if ptr_b.next:
                while ptr_b.next:
                    ptr_a = ptr_a.next
                    ptr_b = ptr_b.next
        # If ptr_b is None, then the node being removed is the head
        else:
            return head.next
        ptr_a.next = ptr_a.next.next
    return head

# Basic case, empty list case, single item case, two item case
tests = [([1, 2, 3, 4, 5], 2), ([], 0), ([1], 1), ([1, 2], 1), ([1, 2], 2)]
for test in tests:
    print("Test case: l = {0}, n = {1}".format(test[0], test[1]))
    head = ListNode(None)
    curr = head
    l, n = test[0], test[1]
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    head = removeNthFromEnd(head.next, n)
    printList(head)