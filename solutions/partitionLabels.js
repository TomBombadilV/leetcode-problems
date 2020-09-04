// Partition Labels

const test = require('./test');

/**
 * Use greedy method
 *
 * @param {string} S
 * @param {number[]}
 */
const partitionLabels = S => {
    if (S == '') {
        return [];
    }
    let [res, lastIndex] = [[], {}];
    i = 0;

    while (i < S.length) {
        // Interval starts and ends with first and last indices of first letter
        let start = i;
        lastIndex[S[i]] = S.lastIndexOf(S[i]);
        let end = lastIndex[S[i]];
    
        // Iterate through all chars in current partition and update end
        while (i <= end) {
            // Check if char exists in lastIndex dictionary
            if (!(S[i] in lastIndex)) {
                lastIndex[S[i]] = S.lastIndexOf(S[i]);
            }
            // Update end if its greater than current end
            if (lastIndex[S[i]] > end) {
                end = lastIndex[S[i]];
            }
            i++;
        }
        res.push(end - start + 1);
    }
    return res;
};

// Driver Code
const cases = [
    ['ababcbacadefegdehijhklij', [9, 7, 8]],
    ['', []],
    ['a', [1]],
    ['ab', [1,1]],
    ['aba', [3]],
    ['happy birthday', [14]]
];
test(cases, partitionLabels);
