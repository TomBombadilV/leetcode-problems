// Repeated Substring Pattern

const test = require('./test');

/** 
 * 1. Substring must always start at beginning character
 * 2. Substring length must be a factor of the string length
 * 
 * @param {string} s
 * @return {boolean}
 */
const repeatedSubstringPattern = s => {
    // Apparently leetcode thinks a string is not a substring of itself
    if (s.length <= 1) {
        return false;
    }
    // Calculate mid. Substring can't be longer than half of string
    const mid = Math.floor(s.length / 2);
    // Try every substring up to halfway point
    for (let i = 0; i < mid; i++) {
        // Check that current substring length is a factor of string length
        if (s.length % (i + 1) == 0) {
            // Create string by repeating substring enough times to match 
            // length of original string
            let s2 = s.slice(0, i + 1).repeat(s.length / (i + 1));
            // If strings match, substring can create original string
            if (s == s2) {
                return true;
            }
        }
    }
    return false;
};
 
// Driver Code
const cases = [['abcadabcadab', false],
               ['abcadabcad', true],
               ['abab', true],
               ['aba', false],
               ['abcabcabcabc', true],
               ['ab', false],
               ['abac', false]
];
test(cases, repeatedSubstringPattern);
