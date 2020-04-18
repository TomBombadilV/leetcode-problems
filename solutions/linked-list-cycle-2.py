# Linked List Cycle
# Using extra space: Save nodes to a dictionary, if encounter a node that 
# already exists in the dic, return that node
#
# Using constant space: Use the same fast/slow pointer algo used to find a 
# cycle. Once you discover that there is a cycle, start one pointer from the 
# beginning and one from teh cycle point and move them at the same speed until 
# they meet
# Time: O(n) | Space: O(1)

from listnode import ListNode, printList

def detectCycle(head: ListNode) -> ListNode:
    if head and head.next and head.next.next:
        # See if cycle exists or not
        slow, fast = head, head
        found = False
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        # No cycle, return null
        if not(found):
            return None
        # Cycle found. Start at found node and head node, increment until head 
        # of cycle is found
        a, b = head, slow
        while not(a == b):
            a, b = a.next, b.next
        return a
    return None

tests = [   ([3, 2, 0, -4], 1, 1), 
            ([1, 2], 0, 0), 
            ([1, 2], -1, None),
            ([1], -1, None),
            ([], -1, None),
            ([1, 2, 3, 4, 5, 6, 7, 2, 3,4 ,22,34, 34, 34, 3, 43,4], -1, None)
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
    res = detectCycle(head)
    print("Passed" if sol == res else "Failed with {0}".format(res))