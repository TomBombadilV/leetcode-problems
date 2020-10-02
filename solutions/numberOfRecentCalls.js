// Number of Recent Calls

const test = require('./test');

class RecentCounter {
    constructor() {
        this.calls = [];
    }

    // Count number of requests made within 3000ms of current request
    ping(t) {
        // Add new time
        this.calls.push(t);

        // Remove all numbers from head of array that are out of range from current time 
        while (this.calls.length > 0 && this.calls[0] < t - 3000) {
            this.calls.shift();
        }

        // Return count of times within range
        return this.calls.length;
    }
}

// Driver Code
let pings = [1, 100, 3001, 3002];
let rc = new RecentCounter();
for (let i = 0; i < pings.length; i++) {
    console.log(rc.ping(pings[i]));
}
