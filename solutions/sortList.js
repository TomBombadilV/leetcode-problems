// Sort List

const test = require('./test');

/**
 * Merge Sort
 * 
 * @param {ListNode} head
 * @return {ListNode}
 */
const sortList = head => {
    const sort = (head, length) => {
        // Don't need to sort if only one node
        if (length <= 1) {
            return head;
        }

        // Split list into two halves
        let mid = Math.ceil(length / 2); 
        // Move to last node of first half
        let curr = head;
        for (let i = 0; i < mid - 1; i++) {
            curr = curr.next;
        }   
        // Save head of second list
        let headB = curr.next;
        // Separate first half from second half
        curr.next = null;

        // Recursively sort first and second halves
        let listA = sortList(head, mid);
        let listB = sortList(headB, length - mid);
            
        // Merge two lists
        let headC = new ListNode(null);
        curr = headC;
        while (listA && listB) {
            if (listA.val <= listB.val) {
                curr.next = listA;
                listA = listA.next;
                curr = curr.next;
                curr.next = null;
            }   
            else {
                curr.next = listB;
                curr = curr.next;
                listB = listB.next;
                curr.next = null;
            }   
        }   
        if (listA) {
            curr.next = listA;
        }   
        if (listB) { 
            curr.next = listB;
        }   
        return headC.next;
    };  

    // Get length of list
    let length = 0;
    let curr = head;
    while (curr) {
        length++;
        curr = curr.next;
    }   
    // Sort it
    return sort(head, length);
};
