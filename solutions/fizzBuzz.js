// Fizz Buzz

/**
  * Original Version
  * @param {Number} n
  * @return {Array[String]} 
  */
const fizzBuzz = n => {
    const s1 = "Fizz";
    const s2 = "Buzz";
    const x = 3;
    const y = 5;
    let res = [];
    for (let i = 1; i <= n; i++) {
        if (i % x == 0 && i % y == 0) {
            res.push(s1 + s2)
        }
        else if (i % x == 0) {
            res.push(s1);
        }
        else if(i % y == 0) {
            res.push(s2);
        }
        else {
            res.push(String(i));
        }
    }
    return res;
};

/**
 * Generalized Version
 *
 * @param {Number} n
 * @return {Array[String]}
 */
const fizzBuzzBetter = n => {
    const [mods, strings] = [[3, 5, 2], ["Fizz", "Buzz", "Moo"]];
    let res = [];
    for (let i = 1; i <= n; i++) {
        let str = "";
        for (let j = 0; j < strings.length; j++) {
            if (i % mods[j] == 0) {
                str += strings[j];
            }
        }
        res.push(str ? str : String(i));
    }   
    return res;
};

console.log(fizzBuzz(15))
console.log(fizzBuzzBetter(15))
