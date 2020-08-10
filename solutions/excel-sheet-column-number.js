// Excel Sheet Column Number
// Time: O(n) | Space: O(1)

const titleToNumber = s => {
    // Sanitize string
    if (s.find(/[^A-Z]/g)) {
        console.log("Please enter valid Excel Title String!");
        return
    }

    let res = 0;
    for (let i = 0; i < s.length; i++) {
        // Go through string from right to left
        let char = s[s.length - i - 1];
        // Convert letter to number
        let charCode = char.charCodeAt() - 64;
        // Based on index, add 26^i * char
        res += 26 ** i * charCode;
    }
    return res;
};

// Driver Code
let s = "ABC";
console.log(titleToNumber(s));
