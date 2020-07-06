// Plus One

const test = require('./test.js');

const plusOne = digits => {
    let carry = 1;
    i = digits.length - 1;
    
    while (carry && i >= 0) {
        let digit = digits[i] + 1;
        digits[i] = digit % 10;
        carry = Math.floor(digit / 10);
        i -= 1;
    }
    
    if (carry) {
        digits.unshift(1);
    }
    
    return digits;
};

const cases = [[[1,2,3],[1,2,4]], [[4,3,2,1],[4,3,2,2]], [[9,9,9],[1,0,0,0]]];
test(cases, plusOne);
