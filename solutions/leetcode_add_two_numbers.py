# LeetCode Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

list1, list2 = [0], [7, 3]
l1, l2 = ListNode(None), ListNode(None)
l1_head, l2_head = l1, l2
for i in list1:
    l1.next = ListNode(i)
    l1 = l1.next
for i in list2:
    l2.next = ListNode(i)
    l2 = l2.next
l1, l2 = l1_head.next, l2_head.next

sumListNode = addTwoNumbers(l1, l2)
while sumListNode:
    print(sumListNode.val)
    sumListNode = sumListNode.next