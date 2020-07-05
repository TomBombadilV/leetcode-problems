// Test module

const checkEquality = (res, expected) => {
    if (typeof res != typeof expected) {
        return false;
    }
    if (typeof res == Array || typeof res == 'object') {
        if (res.length == expected.length &&
                res.every((val, i) => {return val == expected[i]})) {
            return true;
        }
        else {
            return false;
        }
    };
    return res == expected;

};

module.exports = (cases, func) => {
    cases.forEach(c => {
        let args = c.slice(0, c.length - 1);
        let expected = c[c.length - 1];

        let res = func(...args);
        if (checkEquality(res, expected)) {   
            console.log("Passed");
        } else {
            console.log(`Failed ${args} with ${res} expected ${expected}`);
        }  
    });
}
