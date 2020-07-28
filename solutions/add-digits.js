// Add Digits
// Digital Root Formula
// Time: O(1) | Space: O(1)

const test = require('./test.js');

const addDigits = num => {
    return num ? 1 + (num - 1) % 9 : 0;
};

// Driver Code
const cases = [[0, 0], [38, 2], [913042576, 1]];
test(cases, addDigits);
