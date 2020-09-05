// Matrix Diagonal Sum

const test = require('./test');

/**
 * Sum up diagonals, delete middle if matrix has odd number of rows 
 * since middle would be counted twice.
 *
 * @param {number[][]}
 * @return {number}
 */
const diagonalSum = mat => {
    // Sum row by row both diagonals (0 + i, length - i)
    let sum = mat.reduce((sum, row, i) => {
        return sum + row[i] + row[row.length - 1 - i];
    }, 0);
    // Calculate index of middle
    const mid = Math.floor(mat.length / 2);
    // Delete middle if matrix is odd
    return mat.length % 2 == 0 ? sum : sum - mat[mid][mid];
};

// Driver Code
const cases = [
    [[[1,2,3],
      [4,5,6],
      [7,8,9]], 25],
    [[[1,1,1,1],
      [1,1,1,1],
      [1,1,1,1],
      [1,1,1,1]], 8],
    [[], 0],
    [[[5]], 5]
];
test(cases, diagonalSum);
