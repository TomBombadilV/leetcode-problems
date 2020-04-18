from random import shuffle
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

# Builds a random linked list of 0...n-1 with the given size. Returns head node 
def randomList(n: int) -> ListNode:
    head = ListNode(None)
    curr = head
    l = [i for i in range(n)]
    shuffle(l)
    for i in range(n):
        curr.next = ListNode(l[i])
        curr = curr.next
    return head.next
