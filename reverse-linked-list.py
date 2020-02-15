# Reverse Linked List

from listnode import ListNode, printList

# Iterative Solution
def reverseList1(head: ListNode) -> ListNode:
    if not(head):
        return head
    curr, nex = head, head.next 
    curr.next = None
    while nex:
        nex_next = nex.next
        nex.next = curr
        curr = nex
        nex = nex_next
    return curr

# Recursive Solution
def reverseList2(head: ListNode) -> ListNode:
    if head == None:
        return None, None
    if head.next == None:
        return head, head
    prev, new_head = reverseList2(head.next)
    prev.next = head
    head.next = None
    return head, new_head

l = [1, 2, 3, 4, 5]
#l = [1, 2]
#l = []
head = ListNode(None)
curr = head

for i in l:
    curr.next = ListNode(i)
    curr = curr.next
head = head.next
printList(head)
#head = reverseList1(head)
_, head = reverseList2(head)
printList(head)

