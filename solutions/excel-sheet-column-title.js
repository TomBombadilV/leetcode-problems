// Excel Sheet Column Title

const convertToTitle = n => {
    let s = '';
    while (n) {
        let div = Math.floor((n - 1) / 26)
        let mod = (n - 1) % 26;
        s += String.fromCharCode(mod + 1 + 64);
        n = div;
    }
    return s.split('').reverse().join('');
};

// Driver Code
//const cases = [1,26, 28, 701];
let cases = [1000, 1, 26, 27, 28, 703, 702];
cases.forEach(c => {
    console.log(convertToTitle(c));
});
