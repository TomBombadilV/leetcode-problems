# Copy List with Random Pointer
# In first pass, create new nodes and create dictionary with old node as key 
# and new node as value
# Time: O(n) | Space: O(n)

from collections import defaultdict

# For implementation of ListNode with random attribute
def copyRandomList(head: ListNode) -> ListNode:
    curr, prev = head, None
    # Dictionary pointing old nodes to new nodes
    node_dict = defaultdict(ListNode)
    # Head of deep copy
    new_head = None
    # Create list of new nodes, with old random pointers
    while curr:
        # Create new node with val and random of old node
        new = ListNode(curr.val, None, curr.random)
        # Set dict with key of old node with new node
        node_dict[curr] = new
        # If head doesn't exist yet, set to new node
        if not(new_head):
            new_head = new
        # If this isn't the first node (there is a node before this one, set this one to prev
        if prev:
            prev.next = new
        # Move curr to next node
        curr = curr.next
        # Set prev to current new node
        prev = new
    curr = new_head
    while curr:
        # If random pointer is not null
        if curr.random:
            # Change the pointer from the old node to the new node
            curr.random = node_dict[curr.random]
        curr = curr.next

case = [[7,None],[13,0],[11,4],[10,2],[1,0]]