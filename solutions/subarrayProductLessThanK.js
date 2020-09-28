// Subarray Product Less Than K

const test = require('./test');

/**
 * Use 2 pointer approach
 * 
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const numSubarrayProductLessThanK = (nums, k) => {
    let [left, right] = [0, 0];
    let prod = 1;
    let res = 0;

    // Iterate through array
    while (right < nums.length) {
        // Update product of current subarray
        let curr = nums[right];
        prod *= curr;
        // If product exceeds limit, move left pointer until it doesn't'
        if (curr * prod >= k) {
            // If left crosses over right, it will go at most one to the right because
            // once it crosses, curr * prod should become 1 (left<=right check is for if limit
            // is less than 1) and right - left + 1 will become -1 + 1, which is 0
            while (prod >= k && left <= right) {
                prod /= nums[left];
                left++;
            }
        }
        // Add number of subarrays added by current number (which is the current number
        // plus count of all previous numbers in valid subarray)
        res += right - left + 1;
        right++;
    };
    return res;
};

// Driver Code
const cases = [
    [[10,5,2,6], 100, 8],
    [[9,3,4,1,3,6,9,3,1,5,6,9,1], 10, 18],
    [[1,2,3], 0, 0]
];
test(cases, numSubarrayProductLessThanK);
