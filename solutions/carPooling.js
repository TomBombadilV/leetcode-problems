// Car Pooling

const test = require('./test');

/**
 * Sort intervals by starting position. Keep track of current passengers
 * and iterate through all intervals.
 * 
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
const carPooling = (trips, capacity) => {
    let locs = Array(1001).fill(0);
    // Iterate through trips
    for (let i = 0; i < trips.length; i++) {
        let [passengers, start, end] = trips[i];
        // Update loc array with passengers in current trip
        for (let j = start; j < end; j++) {
            locs[j] += passengers;
            // If car capacity exceeded, return False
            if (locs[j] > capacity) {
                return false; 
            }
        };
    }
    return true;
};

// Driver Code
const cases = [
    [[[2,1,5],[3,3,7]], 4, false],
    [[[[2,1,5],[3,3,7]]], 5, true],
    [[[2,1,5],[3,5,7]], 3, true],
    [[[3,2,7],[3,7,9],[8,3,9]], 11, true]
];
test(cases, carPooling);
