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
 *
 * @param {String} word
 * @return {Boolean}
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
 * Pretty short version that uses more space. Compares string to version that
 * is all caps, and version that is all lower case except for first letter.
 *
 * @param {String} word
 * @return {Boolean}
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
test(cases, detectCapitalUse);
test(cases, detectCapitalUsePretty);
