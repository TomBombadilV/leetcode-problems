// Binary Search 

const test = require('./test');

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = (nums, target) => {
    let [left, right] = [0, nums.length - 1];
    while (left <= right) {
        let mid = Math.floor((right + left) / 2);
        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1;
};

// Driver Code
const cases = [
    [[-1,0,3,5,9,12], 9, 4],
    [[-1,0,3,5,9,12], 2, -1]
];
test(cases, search);
