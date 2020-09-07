// Word Pattern

const test = require('./test');

/**
 * Iterate through pattern string and word array at the same time.
 * Track the patterns and their matched words in a dictionary. Track
 * the words that have been matched in a set. Check at each iteration
 * that no pattern that was matched with another word or word that was
 * matched with another pattern becomes matched with something else.
 *
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
const wordPattern = (pattern, str) => {
    let [patternDic, stringSet] = [{}, new Set()];
    const arr = str.split(" ");
    
    // If string and pattern don't match, then there is no pattern
    if (pattern.length != arr.length) {
        return false;
    }
    
    for (let i = 0; i < pattern.length; i++) {
        if (pattern[i] in patternDic) {
            // Char was assigned to another word
            if (patternDic[pattern[i]] != arr[i]) {
                return false;
            }
            // Char was assigned to this word. Do nothing
        }
        else {
            // Word has already been assigned to another character
            if (stringSet.has(arr[i])) {
                return false;
            }
            // Char not encountered before, word not encountered before
            else {
                patternDic[pattern[i]] = arr[i];
                stringSet.add(arr[i]);
            }
        }
    }
    return true;
};

// Driver Code
const cases = [
    ["abba", "dog cat cat dog", true],
    ["abba", "dog cat cat pig", false],
    ["abbc", "dog cat cat dog", false],
    ["aaaa", "dog cat cat dog", false],
    ["aaaa", "dog dog dog dog", true],
    ["abba", "dog dog dog dog", false]
];
test(cases, wordPattern);
