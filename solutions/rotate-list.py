# Rotate List
# Find point of rotation, then change pointers

from listnode import ListNode, buildList, printList

def rotateRight(head: ListNode, k: int) -> ListNode:
    
    # Iterate to tail and find length of list
    tail = head
    count = 1
    
    while tail and tail.next:
        tail = tail.next
        count += 1
    
    # Don't have to rotate if k is 0
    if k % count == 0:
        return head

    # Iterate to node right before point of rotation
    # Point of rotation is k nodes before tail. Previous is k+1 nodes before tail
    k %= count
    ptr = head

    for _ in range(count - k - 1):
        ptr = ptr.next
    
    # Swappy swap
    tail.next = head
    head = ptr.next
    ptr.next = None
    
    return head


# Driver Code
l = [1, 2, 3, 4, 5]
l = []
for i in range(5):
    head = buildList(l)
    printList(rotateRight(head, i))
