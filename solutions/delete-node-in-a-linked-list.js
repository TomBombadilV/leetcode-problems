// Delete Node in a Linked List

const deleteNode = node => {
    node.val = node.next.val;
    node.next = node.next.next;
};

const ListNode = require('./list-node.js')
