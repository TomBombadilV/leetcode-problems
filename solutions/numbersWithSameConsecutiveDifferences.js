// Numbers with Same Consecutive Differences
// Recursion yo

const test = require('./test');

const util = (N, K, num, res) => {
    let minusDigit = num % 10 - K;
    let plusDigit = num % 10 + K;
    if (N == 0) {
        res.push(num);
    }
    if (N > 0) {
        if (minusDigit >= 0 && minusDigit < 10) {
            let temp = util(N - 1, K, num * 10 + minusDigit, res);
        }
        if (K > 0 && plusDigit >= 0 && plusDigit < 10) {
            util(N - 1, K, num * 10 + plusDigit, res);
        }
    }
    return res;
}; 

const numsSameConsecDiff = (N, K) => {
    let res = [];

    // Account for 0
    if (N == 1) { 
        res.push(0);
    }

    for (i = 1; i < 10; i++) {
        util(N - 1, K, i, res);
    }
    return res;
};

let cases = [[3, 7, [181,292,707,818,929]],
             [2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]],
             [0, 0, []],
             [3, 0, [111, 222, 333, 444, 555, 666, 777, 888, 999]],
             [1, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [1, 100, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
];
//cases = [[2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]]];
test(cases, numsSameConsecDiff);
