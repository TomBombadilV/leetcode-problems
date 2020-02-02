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