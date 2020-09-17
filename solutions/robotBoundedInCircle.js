// Robot Bounded in Circle 

const test = require('./test');

/**
 * If robot is facing a different direction at the end of the instruction
 * set, or it ends at the origin, then it will always operate in a circle.
 * 
 * @param {string} instructions
 * @return {boolean}
 */
const isRobotBounded = instructions => {
    // 0 - up, 1 - right, 2 - down, 3 - left
    let [dir, loc] = [0, [0, 0]];

    for (let i = 0; i < instructions.length; i++) {
        // Change direction if facing left or right
        if (instructions[i] == 'L') {
            dir = dir == 0 ? 3 : (dir - 1) % 4;
        }
        else if (instructions[i] == 'R') {
            dir = (dir + 1) % 4;
        }
        // Change location based on direction
        else if (instructions[i] == 'G') {
            if (dir == 0) {
                loc[1]++;
            }
            else if (dir == 1) {
                loc[0]++;
            }
            else if (dir == 2) {
                loc[1]--;
            }
            else if (dir == 3) {
                loc[0]--;
            }
            else {
                // Garbage value
                console.log(dir)
            }
        }
        else {
        // Garbage value
        }
    }
    return dir != 0 || (loc[0] == 0 && loc[1] == 0);
};

// Driver Code
const cases = [
    ['GGLLGG', true],
    ['GG', false],
    ['GL', true],
    ['GLRLLGLL', true]
];
test(cases, isRobotBounded);
