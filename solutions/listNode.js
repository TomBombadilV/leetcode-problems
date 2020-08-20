/** 
  * Linked List implementation
  */
class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

/**
  * Build List
  * Builds a linked list from the given array
  * @param {List} l
  * @return {ListNode}
  */
const buildList = l => {
    if (l.length == 0) {
        return [];
    }
    let head = curr = new ListNode(l[0]);
    for (let i = 1; i < l.length; i++) {
        curr.next = new ListNode(l[i]);
        curr = curr.next;
    }
    return head;
}

/**
  * Print List
  * Prints linked list from given head ListNode
  * @param {ListNode} head
  * @return {void}
  */
const printList = head => {
    let curr = head;
    let list = [];
    while (curr) {
        list.push(curr.val);
        curr = curr.next;
    }
    console.log(...list);
};

module.exports.ListNode = ListNode;
module.exports.buildList = buildList;
module.exports.printList = printList;
