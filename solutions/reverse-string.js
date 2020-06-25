// Reverse String

const reverseString = s => {
    // Don't reverse middle if odd length
    const mid = Math.floor(s.length / 2);
    
    // Swap from front and back until middle
    for (let i = 0; i < mid; i++) {
        const temp = s[i];
        s[i] = s[s.length - i - 1];
        s[s.length - i - 1] = temp;
    }
};

s = ['h', 'e', 'l', 'o'];
reverseString(s);
console.log(s);
