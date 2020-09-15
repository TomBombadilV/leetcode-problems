// Length of Last Word 

const test = require('./test');

/**
 * Split string by space, return length of last word lol
 * 
 * @param {string} s
 * @return {number}
 */
const lengthOfLastWord = s => {
    let words = s.split(' ');
    // Iterate through words from back to front until non-empty word found
    let i = words.length - 1;
    while (i > 0 && words[i].length == 0) {
        i--;
    }
    return words[i].length;
};

// Second method
const lengthOfLastWord2 = s => {
    let words = s.trim().split(' ');
    return words[words.length - 1].length;
};


// Driver Code
const cases = [
    ["Hello World", 5],
    ["", 0],
    ["a", 1],
    ["    ", 0],
    ["a ", 1],
    ["a    ", 1],
    [" a", 1],
    ["     a", 1]
];
test(cases, lengthOfLastWord);
test(cases, lengthOfLastWord2);
