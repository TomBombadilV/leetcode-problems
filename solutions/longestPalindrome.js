// Longest Palindrome
// Is the string sorted?
// If so: 
// Perform linear scan, keeping a running sum of the "floor even" count of each 
// character (ex: if count is 7, floor even count is 6), and keep track of 
// whether an odd count has been encountered. Longest palindrome will be floor 
// even count plus odd flag.
// Time: O(n) | Space: O(1)
// 
// If not:
// Use dictionary to count frequency of each letter. At the end, iterate through 
// dictionary to count "floor even" sum and odd flag.
// Time: O(n) | Space: O(n)

const test = require('./test');

// Sorted method
const longestPalindromeSorted = s => {
    let prev = null;
    let i = 0;
    let sum = 0;
    let count = 0;
    let oddFlag = false;
   
    // Add junk value to end of string to force last character count to be added
    s += '1';

    while (i < s.length) {
        // If characters change, add old count to sum and set oddFlag
        if (s[i] != prev) {
            prev = s[i];
            if (count % 2 == 1) { oddFlag = true; }
            sum += Math.floor(count / 2) * 2; 
            count = 0;
        }
        count++;
        i++;
    }
    return sum + (oddFlag? 1 : 0);
};

// Unsorted method
const longestPalindromeUnsorted = s => {
    // Count frequency of each character
    let charCount = {};
    for (let i = 0; i < s.length; i++) {
        if (charCount[s[i]]) {
            charCount[s[i]]++;
        }
        else {
            charCount[s[i]] = 1;
        }
    }

    // Iterate through ditionary to count floor even and odd flag
    let oddFlag = false;
    let sum = 0;
    Object.keys(charCount).forEach(key => {
        let count = charCount[key];
        if (count % 2 == 1) { oddFlag = true };
            sum += Math.floor(count / 2) * 2;
    });
    return sum + (oddFlag ? 1 : 0);
};

// Driver Code
const cases = [["dad", 3], ["abccccdd", 7], ['a', 1], ['bbcc', 4], ['add', 3]];
//test(cases, longestPalindromeSorted);
test(cases, longestPalindromeUnsorted);
