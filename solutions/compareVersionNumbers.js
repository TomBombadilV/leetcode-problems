// Compare Version Numbers

const test = require('./test');

/**
 * Split into array of numbers. Compare from head while numbers are equal.
 * Then, if numbers are equal, check remaining lengths to see which one
 * is larger.
 *
 * @param {String} version1 
 * @param {String} version2
 * @return {Number}
 */
const compareVersion = (version1, version2) => {
    // Turn versions into arrays of string numbers
    let [v1, v2] = [version1.split('.'), version2.split('.')];
    
    // Iterate through strings to check if they match up. Convert to
    // number to remove leading 0s
    let i = 0;
    while (i < v1.length && i < v2.length) {
        if (Number(v1[i]) < Number(v2[i])) {
            return -1;
        }
        if (Number(v1[i]) > Number(v2[i])) {
            return 1;
        }
        i++;
    }

    // Convert leftover numbers (if one version is longer than the other) to
    // check if it has any value (is more than ex: 0.0.0)
    v1 = Number(v1.slice(i).join(''));
    v2 = Number(v2.slice(i).join(''));

    // Compare remaining value to see if one is larger than the other
    return v1 == v2 ? 0 : (v1 < v2) ? -1 : 1;
}; 

// Driver Code
const cases = [
    ['0.1', '1.1', -1],
    ['1.0.1', '-1', 1],
    ['7.5.2.4', '7.5.3', -1],
    ['1.01', '1.001', 0],
    ['1.0', '1.0.0', 0]
];
test(cases, compareVersion);
