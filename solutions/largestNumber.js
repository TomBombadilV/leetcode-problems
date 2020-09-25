// Largest Number

const test = require('./test');

/**
 * Sort by first digit, then second, etc. Then join as string.
 * Fails for cases where two comparator numbers start and end with same number
 * 
 * @param {number[]} nums
 * @return {string}
 */
const largestNumberBroken = nums => {
    nums = nums.sort((a, b) => {
        let [strA, strB] = [String(a), String(b)];
        let i = 0;
        while (i < strA.length && i < strB.length) {
            if (strA[i] > strB[i]) {
                return -1;
            }
            if (strA[i] < strB[i]) {
                return 1;
            }
            i++;
        }
        // Either a == b or a = b... or b = a... ex: 12 and 123
        if (i < strA.length) {
            if (strA[i] >= strA[0]) {
                return -1;
            }
            else {
                return 1;
            }
        }
        else if (i < strB.length) {
            if (strB[i] >= strB[0]) {
                return 1;
            }
            else {
                return -1;
            }
        }
        else {
            return 0;
        }
    });
    return nums.join('');
};

const largestNumber = nums => {
    nums = nums.sort((a, b) => {
        let [s, t] = [String(a) + String(b), String(b) + String(a)];
        return Number(s) >= Number(t) ? -1 : 1;
    });
    return nums.join('');
}

// Driver Code
const cases = [
    [[10,2], '210'],
    [[3,30,34,5,9], '9534330'],
    [[31,3,2], '3312'],
    [[32,3,1], '3321'],
    [[121, 12], '12121'],
    [[212, 21], '21221']
];
test(cases, largestNumber);
test(cases, largestNumberBroken);
