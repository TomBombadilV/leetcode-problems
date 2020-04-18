# Merge k Sorted Lists
# Sort lists by their first item. Add first list's first item to the solution 
# list, then place the list into the sorted array based on the next node value. 
# Use priority queue
# num lists = k, num items = n => Time: O(klogk + k^2 + n) | Space: O(n)

from typing import List
from listnode import *
from queue import PriorityQueue

def mergeKLists(lists: List[ListNode]) -> ListNode:
    pq = PriorityQueue()
    # Head of solution list
    head = ListNode(None)
    curr = head
    # Add list nodes to priority queue if they aren't null
    for i, l_node in enumerate(lists):
        if l_node:
            # Save the index so there is a secondary value if the first values 
            # are equal
            pq.put((l_node.val, i, l_node))
    # Keep putting the smallest node into the solution list while the pq isn't 
    # empty
    while pq.qsize() > 0:
        n = pq.get()
        curr.next = n[2]
        curr = curr.next
        if curr.next:
            pq.put((curr.next.val, n[1], curr.next))
    return head.next 

# Setting up test cases blah blah blah
test_cases = [  [[1, 4, 5], [1, 3, 4], [2, 6]],
                [[], []],
                [[]],
                [[2, 4, 6, 8], [1, 3, 5, 7]]
            ]
for test_case in test_cases:
    lists = test_case
    listnodes = []
    for l in lists:
        head = ListNode(None)
        curr = head
        for val in l:
            curr.next = ListNode(val)
            curr = curr.next
        listnodes.append(head.next)

    printList(mergeKLists(listnodes))