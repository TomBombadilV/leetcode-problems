// Hamming Distance
// Find number of bits that are different between two numbers
// Go bit by bit

const test = require('./test.js')

const hammingDistance_1 = (x, y) => {
    let res = 0;
    while (x || y) {
        if (x & 1 ^ y & 1) {
            res++;
        }
        x >>= 1;
        y >>= 1
    }
    return res;
};

const hammingDistance_2 = (x, y) => {
    let res = x ^ y;
    return res.toString(2).replace(/0/g, "").length;
}

cases = [[1, 4, 2]];
test(cases, hammingDistance);
