// Arranging Coins

// Intuitive Solution
const arrangeCoins = n => {
    let size = 1;
    while (n >= size) {
        n -= size;
        size += 1;
    }
    return size - 1;
};

// Solution based on n(n+1)/2
const arrangeCoins = n => {
    return Math.floor((Math.sqrt(8 * n + 1) - 1) / 2);
};
