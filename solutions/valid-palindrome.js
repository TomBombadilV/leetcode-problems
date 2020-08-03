// Valid Palindrome
// Method 1:
// Sanitize string (strip spaces, punctuation) and make all lowercase. Then use
// two pointers to check if same front to back, stopping once pointers meet.
// Time: O(n) || Space: O(1)
//
// Method 2:
// Sanitize string, take left and right halves of equal length, check if equal
// Time: O(n) || Space: O(n)

const test = require('./test');

// Method 1
const isPalindrome1 = s => {
    if (s.length == 0 || s.length == 1) {
        return true;
    } 
    s = s.replace(/\W/g, '').toLowerCase();
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
};

// Method 2
const isPalindrome2 = s => {
    // Sanitize string
    s = s.replace(/[_\W]/g, '').toLowerCase();
    
    // Calculate midpoint
    const mid = Math.floor(s.length / 2);
   
    // Slice from left and right
    let left = s.slice(0, mid);
    let right = s.slice(s.length - mid, s.length);
    
    // Reverse right half
    right = right.split('').reverse().join('');
    
    return left == right;
}

const cases = [ ['Hey d00d! d00d yeH', true], 
                ['A man, a plan, a canal: Panama', true],
                ['race a car', false],
                ['', true],
                ['a', true],
                ['ab_a', true]
];

test(cases, isPalindrome2);
