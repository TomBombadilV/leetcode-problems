/** 
  * Goat Latin - Method 1
  * Creates new words array using Array.map
  * @param {string} S
  * @return {string}
  */
const toGoatLatin = S => {
    let words = S.split(' ');
    const vowels = 'aeiouAEIOU';
    words =  words.map((word, i) => {
        if (!vowels.includes(word[0])) {
            word = word.slice(1) + word[0];
        }
        word += 'ma' + 'a'.repeat(i + 1);
        return word;
    });
    return words.join(' ');
};

/**
  * Method 2
  * Changes array in place
  * @param {string} S
  * @return {string}
  */
const toGoatLatin_2 = S => {
    let words = S.split(' ');
    const vowels = 'aeiou';
    
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        if (!vowels.includes(word[0].toLowerCase())) {
            word = word.slice(1) + word[0];
        }
        word += 'ma' + 'a'.repeat(i + 1);
        words[i] = word;
    }
    return words.join(' ');
};

const test = require('./test');

// Driver Code
let cases = [["I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"],
             ["The quick brown fox jumped over the lazy dog", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"]
];
test(cases, toGoatLatin);
test(cases, toGoatLatin_2);
