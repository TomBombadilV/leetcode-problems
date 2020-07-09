// Island Perimeter

const countPerimeter = (grid, i, j) => {
    let count = 0;
    if (i == 0 || grid[i - 1][j] == 0) {
        count++;
    }
    if (i == grid.length - 1 || grid[i + 1][j] == 0) {
        count++;
    }
    if (j == 0 || grid[i][j - 1] == 0) {
        count++;
    }
    if (j == grid[0].length - 1 || grid[i][j + 1] == 0) {
        count++;
    }
    return count;
};

const islandPerimeter = grid => {
    // Make sure grid isn't empty
    if (grid.length == 0 || grid.length[0] == 0) {
        return 0;
    }

    const m = grid.length;
    const n = grid[0].length;

    let perimeter = 0;
    
    // For each number, if it's an island piece, count all adjacent 0s
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                perimeter += countPerimeter(grid, i, j) 
            }
        }
    }
    
    return perimeter;
};

// Driver Code
let grid = [[0,1,0,0],
              [1,1,1,0],
              [0,1,0,0],
              [1,1,0,0]];
console.log(islandPerimeter(grid));

grid = [];
console.log(islandPerimeter(grid));

grid = [[1]];
console.log(islandPerimeter(grid));
