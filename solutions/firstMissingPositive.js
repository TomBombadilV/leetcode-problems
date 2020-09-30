// First Missing Positive

const test = require('./test');

/**
 * Iterate through array, swap each number with its corresponding index as long as the number is 
 * > 0 and <= arr.length. Then iterate through array, and the index of the first number that is not
 * between 0 and arr.length is the first missing positive.
 * 
 * @param {number[]} nums
 * @return {number}
 */
const firstMissingPositive = nums => {
    for (let i = 0; i < nums.length; i++) {
        while (nums[i] > 0 && nums[i] <= nums.length && nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]) {
            let curr = nums[i];
            nums[i] = nums[curr - 1];
            nums[curr - 1] = curr;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != i + 1) {
            return i + 1;
        }
    }
    return nums.length + 1
};


// Driver Code
const cases = [
    [[1,2,0], 3], [[3,4,-1,1], 2], [[7,8,9,11,12], 1], [[], 1], [[1,1], 2]
];
test(cases, firstMissingPositive);
