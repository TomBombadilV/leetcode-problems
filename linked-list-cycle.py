# Linked List Cycle

from listnode import ListNode, printList
from typing import List

tests = [   ([3, 2, 0, -4], 1), 
            ([1, 2], 0), 
            ([1], -1)
        ]
for test in tests:
    print("Test case: {0}".format(test))
    head = ListNode(None)
    curr = head
    for i in test:
        curr.next = ListNode(i)
        curr = curr.next
    head = sortList(head.next)
    printList(head)