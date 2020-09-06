// Image Overlap

const test = require('./test');

/**
 * Convert each row into a bitstring. 
 * Perform shifts of each row to the right (equivalent to shifting Matrix right)
 * Perform shifts of entire rows to the right (equivalent to shifting down)
 * Swap matrices and do the same thing
 *
 * @param {number[][]}
 * @param {number[][]}
 * @return {number}
 */
const largestOverlap = (A, B) => {
    // Converts binary matrix to array of numbers
    const convert = mat => {
        return mat.map(row => { return parseInt(row.join(''), 2) });
    };

    // Counts number of parity bits in two numbers. Converts
    // to bit string, removes 0 bits, returns length
    const countParity = (n, m) => {
        return (n & m).toString(2).replace(/0/g, "").length;
    };
    
    // Move upper left corner of A through all positions in B and check overlap
    const upperCornerOverlap = (A, B) => {
        shiftedA = A;
        maxOverlap = 0;

        // Shift A to the right n times
        for (let i = 0; i < A.length; i++) {
            // Don't shift for the first iteration
            if (i > 0) {
                // Shift matrix to the right
                shiftedA = shiftedA.map(n => { return n >> 1 }); 
            }   
            downShiftedA = shiftedA;
            for (let j = 0; j < A.length; j++) {
                // Shift matrix down
                if (j > 0) {
                    downShiftedA = [0].concat(downShiftedA.slice(0, -1)); 
                }  

                // Compare each row to B matrix to count parity 
                currOverlap = downShiftedA.reduce((sum, n, i) => {
                    return sum + countParity(n, B[i]);
                }, 0); 
                // Update max overlap
                maxOverlap = Math.max(maxOverlap, currOverlap);
            }   
        }   
        return maxOverlap; 
    };

    [A, B] = [convert(A), convert(B)];
    // Do all overlaps of A over B, then all overlaps of B over A
    return Math.max(upperCornerOverlap(A, B), upperCornerOverlap(B, A));
};

const cases = [
    [[[1,1,0],
      [0,1,0],
      [0,1,0]],
     [[0,0,0],
      [0,1,1],
      [0,0,1]], 3],
    [[[0,0,0],
      [0,0,0],
      [0,0,1]],
     [[1,0,0],
      [0,0,0],
      [0,0,0]], 1]
];

test(cases, largestOverlap);
