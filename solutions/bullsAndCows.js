// Bulls and Cows

const test = require('./test');

/**
 * Iterate through both strings. If chars match, increment bull counter.
 * If don't match, keep track of dictionary of char counts of both guess
 * and secret. At the end, find intersection of guess and secret dicts.
 *
 * @param {String} secret
 * @param {String} guess
 * @return {String}
 */
const getHint = (secret, guess) => {
    // Set up dictionaries to count non-matching chars
    let [secretDict, guessDict] = [{}, {}];
    let [bulls, cows] = [0, 0];

    // Count matching and non-matching chars
    for (let i = 0; i < secret.length; i++) {
        let [secretChar, guessChar] = [secret[i], guess[i]];
        // If match, increment bull counter
        if (secretChar == guessChar) {
            bulls++;
        }
        // If no match, count guess and secret chars
        else {
            secretDict[secretChar] = (secretDict[secretChar] || 0) + 1;
            guessDict[guessChar] = (guessDict[guessChar] || 0) + 1;
        }
    }
    
    // Find union of secret and guess chars that didn't line up (this
    // will be the number of correct numbers in the wrong position)
    for (let key in secretDict) {
        if (key in guessDict) {
            cows += Math.min(secretDict[key], guessDict[key]);
        }
    }

    return `${bulls}A${cows}B`;
};

// Driver Code
const cases = [
    ['1807', '7810', '1A3B'],
    ['1123', '0111', '1A1B'],
    ['121212', '212121', '0A6B']
];
test(cases, getHint);
//console.log(getHint(cases[0][0], cases[0][1]));
