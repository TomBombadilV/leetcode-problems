# Odd Even Linked List

from listnode import buildList, ListNode, printList

def oddEvenList(head: ListNode) -> ListNode:
    """
    Move odd to split
    """
    if not(head):
        return head
    split = head
    # Start with even number
    curr = head.next
    while curr and curr.next:
        odd = curr.next
        curr.next = odd.next
        odd.next = split.next
        split.next = odd
        split = odd
        curr = curr.next
    return head

# Driver Code
cases = [[1, 2, 3, 4, 5, 6, 7, 8],
         [2, 1, 3, 5, 6, 4, 7],
         [1],
         []
]

for l in cases:
    head = buildList(l)
    printList(oddEvenList(head))
