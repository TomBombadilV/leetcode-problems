# Palindrome Linked List
# Get length of list in first pass. In second pass, reverse half of the linked 
# list, then with the two head pointers, compare to see if the lists are equal
# Time: O(n) | Space: O(1)

from listnode import ListNode

def isPalindrome(head: ListNode) -> bool:
    curr = head
    # Get length of list
    l = 0
    while curr:
        l += 1
        curr = curr.next
    # Get middle index of list
    mid = l // 2
    # Move pointer to middle of list
    i = 0
    curr, prev = head, None
    while i < mid:
        i += 1
        prev = curr
        curr = curr.next
    # Reverse second half of list
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    # Check if vals are equal
    head2 = prev
    for _ in range(mid):
        if head.val != head2.val:
            return False
        head, head2 = head.next, head2.next
    return True

cases = [   ([1, 2], False), 
            ([1, 2, 2, 1], True), 
            ([], True), 
            ([1], True), 
            ([1, 2, 3], False), 
            ([1, 3, 1], True),
            ([1, 1], True),
            ([1, 2, 3, 4, 5, 4, 3, 2, 1], True)
        ]

for case in cases:
    arr, ans = case
    head = ListNode(None)
    curr = head
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next
    head = head.next
    res = isPalindrome(head)
    print("Passed" if res == ans else "Failed {0} with {1} expected {2}".format(arr, res, ans))