// Reverse String

const reverseString = s => {
    const mid = Math.floor(s.length / 2);
    for (let i = 0; i < mid; i++) {
        const temp = s[i];
        s[i] = s[s.length - i - 1];
        s[s.length - i - 1] = temp;
    }
};

s = ['h', 'e', 'l', 'o'];
reverseString(s);
console.log(s);
