// Detect Capital

/**
 * Original version written before I realized all lowercase is a valid case too :P
 * 
 * Detect if a word is either all caps, or all not caps except for the first letter.
 * Check first letter is caps. Then check the case of each letter against the case of
 * the second letter.
 *
 * @param {String} word
 * @return {Boolean}
 */
const detectCapitalUseOriginal = word => {
    // Check that first letter is capitalized
    if (word.length > 0 && word[0] != word[0].toUpperCase()) {
        return false;
    }
    // If word is 0, 1, 2 letters long, then case of second letter doesn't matter
    if (word.length <= 2) {
        return true;
    }
    // Get case of second letter
    let allCaps = word[1] == word[1].toUpperCase();

    // Check case of all other letters against case of second letter
    for (let i = 2; i < word.length; i++) {
        if ((word[i] == word[i].toUpperCase()) != allCaps) {
            return false;
        }
    }
    return true;
};

/** 
 * New version to include all lowercase case
 */
const detectCapitalUse = word => {
    // Don't need to check if word is 0 or 1 char long
    if (word.length <= 1) {
        return true;
    } 
    
    // Get expected case based off of first two characters. 
    // If both upper, expect upper. If first upper and second lower, expect lower.
    // If both lower, expect lower. Case of first lower and second upper 
    // will be handled during iterations. Value is true if upperCase expected
    let expected = word[0] == word[0].toUpperCase() && word[1] == word[1].toUpperCase();
    
    // Check that every letter after the first one is the expected case
    for (let i = 1; i < word.length; i++) {
        if ((word[i] == word[i].toUpperCase()) != expected) {
            return false;
        } 
    }
    return true;
};

/**
 * Method using Regex 
 */
const detectCapitalUseRegex = word => {
    // Using * instead of + for [A-Z] rule to test for empty string
    return /^([A-Z][a-z]+|[A-Z]*|[a-z]+)$/.test(word);
};

/**
 * Method using sums
 */
const detectCapitalUseSum = word => {
    if (word.length <= 1) {
        return true;
    }
    // Count how many uppercase letters exist
    let upperSum = 0;
    for (let i = 0; i < word.length; i++) {
        if (word[i] == word[i].toUpperCase()) {
            upperSum++;
        }
    }
    // Get case of first letter
    let firstIsUpper = word[0] == word[0].toUpperCase();
    
    // If first letter lowercase, sum must be 0.
    // If first letter uppercase, sum must be 1 or word length.
    if ((!firstIsUpper && upperSum > 0) || 
        (firstIsUpper && (upperSum > 1 && upperSum < word.length))) {
        return false;
    }
    return true;
};

/**
 * Pretty short version that uses more space. Compares string to version that
 * is all caps, and version that is all lower case except for first letter.
 */
const detectCapitalUsePretty = word => {
    return word == word.toUpperCase() || 
        word == word.toLowerCase() ||
        word == word[0].toUpperCase() + word.slice(1).toLowerCase();
};

const test = require('./test');
const cases = [['', true], ['S', true], ['s', true], ['USA', true], 
               ['uSA', false], ['uSA', false], ['usa', true], 
               ['USa', false], ['UsA', false], ['Usa', true]];
//test(cases, detectCapitalUse);
//test(cases, detectCapitalUseRegex);
test(cases, detectCapitalUseSum);
//test(cases, detectCapitalUsePretty);
