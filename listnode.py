from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Helper function to print list node values in a row
def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Builds a linked list with the given list of values. Returns head node
def buildList(l: List) -> ListNode:
    head = ListNode(None)
    curr = head
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    return head.next
