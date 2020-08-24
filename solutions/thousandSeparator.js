// Thousand Separator
// Time: O(n) | Space: O(n)

const test = require('./test');

/**
 * Method 1: Cast number to string, then iterate
 * Takes a number and places separators for every group of 3 digits
 *
 * @param {Number} n
 * @return {String} s
 */
const thousandSeparator = n => {
    let s = String(n);
    let i = s.length - 1;
    let count = 0;
    // Iterate through string from end to start
    while (i >= 0) {
        count++;
        // If you reach a number that comes BEFORE a separator, add the separator after current number
        if (count == 4) {
            s = s.slice(0, i + 1) + '.' + s.slice(i + 1);
            count = 0;
        } 
        else {
            i--;
        }
    }
    return s;
};

/** 
 * Method 2: Use % 1000 to get groups of 3
 * Takes a number and places separators for every group of 3 digits.
 * 
 * @param {Number} n
 * @return {String} s
 */
const thousandSeparator2 = n => {
    let res = "";
    while (n > 999) {
        let curr = n % 1000;
        n = Math.floor(n / 1000);
        // Must pad current chunk in case it had leading zeroes
        res = '.' + String('000' + curr).slice(-3) + res;
    }
    res = n + res;
    return res;
};

// Driver Code
const cases = [[987,        "987"],
               [1234,       "1.234"],
               [123456789,  "123.456.789"],
               [0,          "0"],
               [51040,      "51.040"]
];
test(cases, thousandSeparator2);
