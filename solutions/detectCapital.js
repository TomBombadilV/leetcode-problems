// Detect Capital

/** 
 * Detect if a word is either all caps, or all not caps except for the first letter.
 * Check first letter is caps. Then check the case of each letter against the case of
 * the second letter.
 *
 * @param {String} word
 * @return {Boolean}
 */
const detectCapitalUse = word => {
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
 * Pretty short version that uses more space. Compares string to version that
 * is all caps, and version that is all lower case except for first letter.
 *
 * @param {String} word
 * @return {Boolean}
 */
const detectCapitalUsePretty = word => {
    
    return word == word.toUpperCase() || 
        word == word[0].toUpperCase() + word.slice(1).toLowerCase();
};

const test = require('./test');
const cases = [['', true], ['S', true], ['s', false], ['USA', true], 
               ['uSA', false], ['uSA', false], ['usa', false], 
               ['USa', false], ['UsA', false], ['Usa', true]];
test(cases, detectCapitalUse);
test(cases, detectCapitalUsePretty);
