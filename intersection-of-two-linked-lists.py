# Intersection of Two Linked Lists
# Traverse to the end of the lists to get their lengths and make sure they actually intersect. Get difference in lengths, then 
# Time: O(n) | Space: O(1)

from listnode import ListNode, printList

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # If either list is empty, there is no intersection
    if not(headA) or not(headB):
        return None
    # Get lengths of lists
    len_a, len_b = 0, 0
    a, b = headA, headB
    while a.next:
        len_a += 1
        a = a.next
    while b.next:
        len_b += 1
        b = b.next
    # If tails are not the same, then there is no intersection
    if not(a == b):
        return None
    # Move the pointer of the list that is longer until both pointers are same 
    # distance from intersection node
    a, b = headA, headB
    if len_a > len_b:
        for _ in range(len_a - len_b):
            a = a.next
    if len_a < len_b:
        for _ in range(len_b - len_a):
            b = b.next
    # Move both pointers together until they are at the same node
    while not(a == b):
        a, b = a.next, b.next
    # Return intersection node
    return a
    

tests = [   ([4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3, 8), 
            ([0, 9, 1, 2, 4], [3, 2, 4], 3, 1, 2), 
            ([2, 6, 4], [1, 5], 3, 2, None)
        ]

for test in tests:
    # Unpack test values
    arr_a, arr_b, skip_a, skip_b, sol = test
    # Create un-intersected portion of lists
    head_a, head_b = ListNode(None), ListNode(None)
    curr_a, curr_b = head_a, head_b
    for i in range(skip_a):
        curr_a.next = ListNode(arr_a[i])
        curr_a = curr_a.next
    for i in range(skip_b):
        curr_b.next = ListNode(arr_b[i])
        curr_b = curr_b.next
    # If there is an intersected section of the lists, create them
    if sol:
        # Create intersection node
        intersection_node = ListNode(arr_a[skip_a])
        # Point both lists to this node
        curr_a.next, curr_b.next = intersection_node, intersection_node
        # Create the rest of the list
        for i in range(skip_a+1, len(arr_a)):
            intersection_node.next = ListNode(arr_a[i])
            intersection_node = intersection_node.next
    # Throw away null node
    head_a, head_b = head_a.next, head_b.next
    # Check lists
    printList(head_a)
    printList(head_b)
    # Run intersection function to get intersection node
    res = getIntersectionNode(head_a, head_b)
    res = res if not(res) else res.val
    print("Passed" if sol == res else "Failed with {0}".format(res))