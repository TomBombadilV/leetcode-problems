// Distribute Candies to People
// Brute Force Method: Keep incrementally distributing.
// Time: O(candies) || Space: O(people)
//
// Math Method: Use n(n+1)/2 formula to calculate number of turns needed to distribute
// all of the candies. Calculate 
// Time: O(min(candies, people)) || Space: O(people)

const test = require('./test');

const distributeCandiesBruteForce = (candies, numPeople) => {
    let i = 1;
    let curr = 0;
    let sum = 0;
    let res = Array(numPeople).fill(0);
    while (sum <= candies - i) {
        res[curr] += i;
        sum += i;
        i++;
        curr = (curr + 1) % numPeople;
    }
    res[curr] += candies - sum;
    return res;
};

const distributeCandies = (candies, numPeople) => {
    // Calculate and fill initial array
    let res = Array(numPeople).fill(0);
    let turns = Math.floor(Math.sqrt(2 * candies) / numPeople);
    let sum = (numPeople * turns) * ((numPeople * turns) + 1) / 2;
    if (sum <= candies) {
        let start = (sum / numPeople) - (turns * (numPeople - 1) / 2);
        for (let i = 0; i < numPeople; i++) {
            res[i] = start + (i * turns);
        }
    } else {
        turns = 0;
        sum = 0;
    }
    // Fill remaining candies
    let i = (numPeople * turns) + 1;
    let curr = 0;
    while (sum <= candies - i) { 
        res[curr] += i;
        sum += i;
        i++;
        curr = (curr + 1) % numPeople;
    }   
    res[curr] += candies - sum;
    return res;
};

let cases = [[7, 4, [1, 2, 3, 1]],
             [10, 3, [5, 2, 3]],
             [100, 3, [35, 35, 30]],
             [100, 4, [28, 27, 21, 24]],
             [5, 10, [1, 2, 2, 0, 0, 0, 0, 0, 0, 0]],
             [800, 40, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,20]]
];
test(cases, distributeCandiesBruteForce);
test(cases, distributeCandies);
