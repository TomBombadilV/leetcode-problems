// Reorder List
// Find length and midpoint of list. Reverse second half of list. Interweave
// both halves of list.
// Time: O(n) | Space: O(1)

const list = require('./listNode.js');

/**
  * Reorder List
  * @param {ListNode} head
  * @return {void}
  */
const reorderList = head => {
    // Ignore all cases where we don't have two halves of the list (list is length 0 or 1)
    if (!head || !head.next ) {
        return;
    }
    
    // Find midpoint of list
    let pA = head;
    let len = 0;
    while (pA) {
        len++;
        pA = pA.next;
    }
    mid = Math.ceil(len / 2) - 1;
    
    // Move pA to middle node
    pA = head;
    for (let i = 0; i < mid; i++) {
        pA = pA.next; 
    }
    
    // Break connection between two halves
    let temp = pA.next;
    pA.next = null;
    pA = temp;

    // Reverse second half of list
    pB = pA.next;
    pA.next = null;
    while (pB) {
        let temp = pB.next;
        pB.next = pA;
        pA = pB
        pB = temp;
    }

    // Weave two lists
    pB = pA
    pA = head;
    
    while (pA && pB) {
        let nextA = pA.next;
        let nextB = pB.next;
        pA.next = pB;
        pB.next = nextA;
        pA = nextA
        pB = nextB;
    }
};

let cases = [[1, 2, 3], [1], [], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5,6,7]];
cases.forEach(c => {
    let head = list.buildList(c);
    // Print original list
    process.stdout.write("Before ordering: ")
    list.printList(head);
    // Reorder list
    reorderList(head);
    // Print new list
    process.stdout.write("After ordering: ")
    list.printList(head);
    console.log("-------")
});
