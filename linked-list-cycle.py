# Linked List Cycle
# Time: O(n) | Space: O(1)

from listnode import ListNode, printList

def hasCycle(head: ListNode) -> bool:
    if head:
        slow, fast = head, head.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
    return False

tests = [   ([3, 2, 0, -4], 1, True), 
            ([1, 2], 0, True), 
            ([1, 2], -1, False),
            ([1], -1, False),
            ([], -1)
        ]
for test in tests:
    arr, cycle_i, sol = test
    # Create list out of input array
    head = ListNode(None)
    curr = head
    cycle_node = None
    for i, n in enumerate(arr):
        curr.next = ListNode(n)
        curr = curr.next
        # Save node that tail points to
        if i == cycle_i:
            cycle_node = curr
    # Set tail to point to cycle node
    curr.next = cycle_node
    # Throw away null node
    head = head.next
    print("Passed" if sol == hasCycle(head) else "Failed with {0}".format(not(sol)))