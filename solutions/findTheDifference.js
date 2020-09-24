// Find the Difference
// Method 1: 
// Sort s and t. Iterate through t until it doesn't match s
// Time: O(slogs + tlogt) | Space: O(1)
//
// Method 2: 
// Turn s and t into character count dictionaries. Find difference.
// Time: O(s + t) | Space: O(s + t)
//
// *Can't use sets, because extra character might be a repeat of an existing letter
//
// Method 3:
// XOR the characters from s and t

const test = require('./test');

/**
 * @param {string} s
 * @param {string} t
 * @param {character}
 */
const findTheDifference = (s, t) => {
    let [xorS, xorT] = [0, 0];
    // XOR all chars in s
    for (let i = 0; i < s.length; i++) {
        xorS ^= s.charCodeAt(i);

    }
    // XOR all chars in t
    for (let i = 0; i < t.length; i++) {
        xorT ^= t.charCodeAt(i);
    }
    // xor results from s and t to get unique character
    return String.fromCharCode(xorS ^ xorT)
};

// Driver Code
const cases = [
    ['abcd', 'abcde', 'e'],
    ['aaaa', 'aaaaa', 'a'],
    ['', 'b', 'b'],
    ['b', 'bb', 'b']
];
test(cases, findTheDifference);
