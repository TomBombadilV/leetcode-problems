# Merge two sorted lists recursively

from listnode import *

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not(l1):
        return l2
    if not(l2):
        return l1
    # Both l1 and l2 exist
    if l2.val < l1.val:
        l2.next = mergeTwoLists(l1, l2.next)
    else:
        l1.next = mergeTwoLists(l1.next, l2)
