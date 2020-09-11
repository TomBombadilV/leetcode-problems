// Maximum Product Subarray

const test = require('./test');

/** 
 * Iterate through array, keeping track of max and min products including current 
 * number (compare using just current number or including previous values)
 * 
 * @param {number[]} nums
 * @return {number}
 */
const maxProduct = nums => {
    if (nums.length < 1) {
        return null;
    }

    // Minimum at the start is the first number
    let res = nums[0];
    // Array to keep track of max and min at each index
    let dp = [[nums[0], nums[0]]];
    
    // Iterate through array and compare current number, current number x previous
    // max, current number x previous min
    for (let i = 1; i < nums.length; i++) {
        let min = Math.min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i]);
        let max = Math.max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i]);
        dp.push([min, max]);
        res = Math.max(res, min, max);
    }
    return res;
};

// Driver Code
const cases = [
    [[2, 3, -2, 4], 6],
    [[-2, 0, -1], 0],
    [[-2, 3, 4, 5, 6, 7, -8], 40320],
    [[-2], -2]
];
test(cases, maxProduct);
//console.log(maxProduct(cases[0][0]));
