# Swap nodes of a linked list in pairs

from listnode import *

def swapPairs(head: ListNode) -> ListNode:
    if head and head.next:
       # Get pair to be swapped
       left, right = head, head.next
       # Swap
       left.val, right.val = right.val, left.val
       # Recurse
       swapPairs(right.next)
    return head

# Driver Code
l = [1, 2, 3, 4, 5]
head = ListNode(None)
curr = head
for i in l:
    curr.next = ListNode(i)
    curr = curr.next
head = head.next
printList(head)
swapPairs(head)
printList(head)
