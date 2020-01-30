# Remove Nth Node From End of List
# Have two pointers n distance apart. When second pointer reaches end of list, 
# first pointer will be n from end
# Time: O(n) | Space: O(1)

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head:
        ptr_a, ptr_b = head, head
        for i in range(n):
            ptr_b = ptr_b.next
        if ptr_b:
            if ptr_b.next:
                while ptr_b.next:
                    ptr_a = ptr_a.next
                    ptr_b = ptr_b.next
        else:
            return head.next
        ptr_a.next = ptr_a.next.next
    return head

def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Basic case, empty list case, single item case, two item case
tests = [([1, 2, 3, 4, 5], 2), ([], 0), ([1], 1), ([1, 2], 1), ([1, 2], 2)]
#tests = [([1, 2, 3, 4, 5], 2)]
for test in tests:
    print("Test case: l = {0}, n = {1}".format(test[0], test[1]))
    head = ListNode(None)
    curr = head
    l, n = test[0], test[1]
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    head = removeNthFromEnd(head.next, n)
    printList(head)