# Add Two Numbers
# Time: O(n) | Space: O(n)

from listnode import ListNode

def addDigits(curr_sum, sum_list):
    carry = curr_sum // 10
    sum_list.next = ListNode(curr_sum % 10)
    sum_list = sum_list.next
    return carry, sum_list

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    sum_list = ListNode(None)
    sum_list_head = sum_list
    carry = 0
    while l1 and l2:
        curr_sum = l1.val + l2.val + carry
        carry, sum_list = addDigits(curr_sum, sum_list)
        l1, l2 = l1.next, l2.next
    while l1:
        curr_sum = l1.val + carry
        carry, sum_list = addDigits(curr_sum, sum_list)
        l1 = l1.next
    while l2:
        curr_sum = l2.val + carry
        carry, sum_list = addDigits(curr_sum, sum_list)
        l2 = l2.next
    if carry:
        sum_list.next = ListNode(1)
        sum_list = sum_list.next
    return sum_list_head.next