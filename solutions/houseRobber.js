// House Robber 

const test = require('./test');

/**
 * Iterate through array, keeping track of max including current and 
 * not including current.
 *
 * @param {number[]} nums
 * @return {number}
 */
const rob = nums => {
    // Keep track of current value including and excluding current number
    let [inc, exc] = [0, 0];
    
    for (let i = 0; i < nums.length; i++) {
        tempExc = exc;
        // Excluding current number, the max will be the larger
        // of the prior including / excluding values
        exc = Math.max(inc, exc);
        // Including current number will be the previous max excluding
        inc = tempExc + nums[i];
    }
    // Max including and excluding last number
    return Math.max(inc, exc);
};

// Driver Code
const cases = [
    [[1, 2, 3, 1], 4],
    [[2, 7, 9, 3, 1], 12],
    [[], 0],
    [[2], 2],
    [[10, 3, 6, 8, 1], 18]
];
test(cases, rob);
