// Complement of Base 10 Integer

const test = require('./test');

/**
 * Method 1: Flip each bit manually
 *
 * @param {number} N
 * @return {number}
 */
 const bitwiseComplementOld = N => {
    let bin = parseInt(N, 10).toString(2).split('');
    for (let i = 0; i < bin.length; i++) {
        bin[i] = bin[i] == '1' ? '0' : '1';
    }
    return parseInt(bin.join(''), 2);
 };

/**
 * Method 2: Find power of 2 closest to N. Subtract N + 1 to get complement
 */
const bitwiseComplement = N => {
    // Get smallest power of 2 that is larger than N
    // Add 1 to N because if N is a power of 2, we need the next largest power of 2
    let leadingBit = 2 ** (Math.ceil(Math.log(N + 1) / Math.log(2)));
    // Zero is weird because log(1) is 0
    return N == 0 ? 1: leadingBit - N - 1;
}


// Driver Code
const cases = [
    [5, 2], [7, 0], [10, 5], [0, 1], [2, 1]
];
test(cases, bitwiseComplementOld)
test(cases, bitwiseComplement);
