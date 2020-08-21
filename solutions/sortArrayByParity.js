// Sort Array by Parity
// Keep track of divide of even and odd numbers. Whenever even number is encountered,
// swap with the odd number at the divide and increment the divide.
// Time: O(n) | Space: O(1)

const test = require('./test');

/**
  * @param {number[]} A
  * @return {number[]} A
  */
const sortArrayByParity = A => {
    // Keep track of divide
    let odd = 0;
    for (let i = 0; i < A.length; i++) {
        // If current number is even
        if (A[i] & 1 ^ 1) {
            // Swap with divide
            let temp = A[i];
            A[i] = A[odd];
            A[odd] = temp;
            // Move divide to the right
            odd++;
        }
    }
    return A;
};

// Driver Code
const cases = [[[3, 1, 2, 4], [2, 4, 3, 1]],
               [[1, 2, 3, 4], [2, 4, 3, 1]],
               [[2, 4, 1, 3], [2, 4, 1, 3]],
               [[1, 3, 2, 4], [2, 4, 1, 3]],
               [[], []],
               [[1], [1]]
];
test(cases, sortArrayByParity);
