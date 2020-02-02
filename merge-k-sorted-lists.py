# Merge k Sorted Lists
# Sort lists by their first item. Add first list's first item to the solution 
# list, then place the list into the sorted array based on the next node value
# num lists = k, num items = n => Time: O(klogk + k^2 + n) | Space: O(n)

from typing import List
from listnode import *

def mergeKLists(lists: List[ListNode]) -> ListNode:
    # Remove null lists
    lists = [l for l in lists if l]
    # If lists is empty, return a null ListNode
    if not(lists):
        return ListNode(None).next
    # Sort the lists by the value of their head node
    lists = sorted(lists, key=lambda x: x.val)
    # Create solution list
    solution_head = ListNode(None)
    curr = solution_head
    # While lists still exist in the array
    while lists:
        # Add the smallest value to the solution list
        curr.next = ListNode(lists[0].val)
        curr = curr.next
        # If the chosen list has a next node, set the head to that
        if lists[0].next:
            lists[0] = lists[0].next
            # Move the list with the new head node value to where it belongs in
            # the sorted list
            ptr = 1
            while ptr < len(lists) and lists[0].val > lists[ptr].val:
                ptr+=1
            lists = lists[1:ptr] + [lists[0]] + lists[ptr:len(lists)]
        # If doesn't have a next node, remove the list from the array
        else:
            lists = lists[1:]
    return solution_head.next

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