# Remove Duplicates from Sorted List

from listnode import ListNode, printList

def deleteDuplicates(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

head = curr = ListNode(None)
l = [1, 1, 2, 3, 3, 4, 5, 6, 6]
for n in l:
    curr.next = ListNode(n)
    curr = curr.next
printList(deleteDuplicates(head.next))
