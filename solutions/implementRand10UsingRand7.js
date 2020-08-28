// Implement Rand10() Using Rand7()

const rand7 = () => { return Math.floor(Math.random() * 7) + 1 };

const rand10 = () => {
    // Map out numbers 7 * (0 ~ 6) + (0 ~ 6) so they are evenly distributed over 0 ~ 48
    let n = (rand7() - 1) * 7 + (rand7() - 1);
    // 40 ~ 48 is not uniformly distributed over 1 ~ 10, so ignore those numbers
    if (n >= 40) {
        return rand10();
    }
    // Shift 0 ~ 39 to 1 ~ 40, mod by 10 to get 1 ~ 10 range
    return n % 10 + 1;
};

let dist = {};
const n = 10000000;
for (let i = 0; i < n; i++) {
    let res = rand10()
    if (res in dist) { dist[res]++ }
    else { dist[res] = 1 }
}
console.log(dist)
