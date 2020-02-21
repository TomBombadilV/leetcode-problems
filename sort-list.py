# Sort List
# Modified mergesort
# Time: O(nlogn) | Space: O(1)

from listnode import ListNode, printList
from typing import List

def sortList(head: ListNode) -> ListNode:
    if not(head):
        return head
    # Count number of nodes in list
    curr, n = head, 0
    while curr:
        n += 1
        curr = curr.next
    return recurse(n, head)

def recurse(n: int, head: ListNode) -> ListNode:
    # If list is len 1, return
    if head.next == None:
        return head
    curr, left, right = ListNode(None), head, head
    # New head of list, in case head is not left node
    new_head = curr
    # Send right pointer to the beginning of the right half of the list
    for _ in range(n//2 - 1):
        right = right.next
    # Stop the left half from pointing to the right half
    temp = right
    right = right.next
    temp.next = None
    # Mergesort left and right halves of the list
    left = recurse(n//2, left)
    right = recurse(n//2, right)
    # Combine left and right
    while left and right:
        # If left is smaller, point to left node and move left pointer to next
        if left.val < right.val:
            curr.next = left 
            curr = curr.next
            left = left.next
        # If right is saller, point to right node and move right pointer to next
        else: 
            curr.next = right
            curr = curr.next
            right = right.next
    # If nodes still remain in either left or right, add to list
    if right:
        curr.next = right
    if left:
        curr.next = left
    return new_head.next

# Basic case, empty list case, single item case, two item case
tests = [[2, 1], [3, 2, 1], [4, 2, 1, 3], [1, 5, 3, 4, 0], [], [1], [1, 2]]
for test in tests:
    print("Test case: {0}".format(test))
    head = ListNode(None)
    curr = head
    for i in test:
        curr.next = ListNode(i)
        curr = curr.next
    head = sortList(head.next)
    printList(head)