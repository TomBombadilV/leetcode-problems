# Reverse Nodes in k-Group
# Time: O(n) | O(1)
from listnode import ListNode, buildList, printList

def checkLen(head, k):
    curr, count = head, 0
    while curr and count < k:
        count += 1
        curr = curr.next
    return count == k

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    Iterative Method
    """
    # Make sure input is valid
    if k <= 1 or not(head):
        return head

    # New list head and tail of previous group
    real_head, prev_tail = None, None

    # Make sure at least k more nodes in list
    while checkLen(head, k):
        count = 1
        old_head, new_head, curr = head, head, None
        while count < k and old_head.next:
            curr = old_head.next
            old_head.next = curr.next
            curr.next = new_head
            new_head = curr
            count += 1
        real_head = new_head if not(real_head) else real_head
        head = old_head.next
        if prev_tail:
            prev_tail.next = new_head
        prev_tail = old_head
    return real_head if real_head else head

#def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    Recursive Method
    """
    


# Driver Code
l = [1, 2, 3, 4, 5]
head = buildList(l)
head = reverseKGroup(head, 6)
printList(head)
