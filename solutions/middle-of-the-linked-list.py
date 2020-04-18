# Given a non-empty, singly linked list, return the middle node of the linked
# list. If two middle nodes, return the second one.

from listnode import *

def middleNode(head: ListNode) -> ListNode:
    # Get length of list
    l = 0
    curr = head
    while curr:
        curr = curr.next
        l += 1
    curr = head
    # Go to middle index
    l = l // 2
    while l > 0:
        curr = curr.next
        l -= 1
    return curr

# Driver code
l = [0, 1]
head = buildList(l)
print(middleNode(head).val)
