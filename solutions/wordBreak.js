// Word Break

const test = require('./test');

/** 
 * DP
 *
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = (s, wordDict) => {
    // Convert array to set
    const convertArrToSet = arr => {
        let set = new Set();
        arr.map(word => { set.add(word) });
        return set;
    };

    const set = convertArrToSet(wordDict);

    // DP array for all words that end at given index
    let dp = new Array(s.length + 1).fill(false);
    dp[0] = 1;

    // Iterate through, checking for all substrings ending at current
    // index. If it ends there, and a valid substring ends at 
    // beginning index, it is valid.
    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && set.has(s.substring(j, i))) {
                dp[i] = true;
            }
        }
    }
    return dp[s.length];
};

/**
 * Convert word dict to actual dict lol. Go from O(logn) to O(1) lookup. Takes
 * O(words) processing step.
 * Backtracking method. Times out :(
 * 
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreakOld = (s, wordDict) => {
    // Convert array to set
    const convertArrToSet = arr => {
        let set = new Set();
        arr.map(word => { set.add(word) });
        return set;
    }; 
    
    const set = convertArrToSet(wordDict);

    let i = 0;
    let curr = '';
    let words = [];
    
    while (i < s.length) {
        // Iterate through string once   
        while (i < s.length - 1) {
            curr += s[i];
            if (set.has(curr)) {
                words.push([curr, i]);
                curr = '';
            }
            i++;
        }
        // Add last letter
        curr += s[i];
        // If word is not in set 
        if (!(set.has(curr))) {
            // Backtrack to last word saved 
            if (words.length > 0) {
                [curr, i] = words.pop();
            }
            // If no words saved, then no words exist
            else {
                return false;
            }
        }
        // If curr was in set, this pushes index past end of string and leaves while loop
        // If curr was not in set, this moves index past index of last saved word
        i++;
    }
    return true;
};

// Driver Code
const cases = [
    ['leetcode', ["leet", "code"], true],
    ['applepenapple', ["apple", "pen"], true],
    ['catsandog', ["cats", "dog", "sand", "and", "cat"], false],
    ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], false]

];
test(cases, wordBreak);
//console.log(wordBreak(cases[2][0], cases[2][1]));
