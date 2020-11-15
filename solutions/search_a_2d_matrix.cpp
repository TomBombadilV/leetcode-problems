// Search a 2D Matrix
// Doing binary search on the entire list would be O(m*n).
// Doing binary search on row then column would be O(m) + O(n).

#include <iostream>
#include <vector>

/*
 * Basic binary search on the given row
 */
bool searchRow(std::vector<int> &row, int target) {
    int left = 0;
    int right = row.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (row[mid] == target) {
            return true;
        }
        else if (row[mid] > target) {
            right = mid - 1;
        }
        else {  // row[mid] < target
            left = mid + 1;
        }
    }

    return false;
}

bool search(std::vector<std::vector<int>> &matrix, int target) {
    
    // Check that  matrix is not empty
    if (matrix.size() == 0 || matrix[0].size() == 0) {
        return false;
    }
     
    int left = 0;
    int right = matrix.size() - 1;
    
    // Binary search beginning of rows
    while (left <= right) {
        int mid = (right + left) / 2;

        // If beginning of mid row is target
        if (matrix[mid][0] == target) {
            return true;
        }
        // If beginning of mid row is larger and is NOT the first row, look left
        else if (matrix[mid][0] > target && mid != 0) {
            right = mid - 1;
        }
        // If beginning is smaller and is NOT the last row and next row is not larger, look right
        else if (matrix[mid][0] < target && mid != matrix.size() - 1 &&
            matrix[mid + 1][0] <= target){ // matrix[mid][0] < target
            left =  mid + 1;
        }
        // If beginning is smaller (may be last row or next row is less than or equal to), search row
        else if (matrix[mid][0] < target) {
            return searchRow(matrix[mid], target);
        }
        // If beginning is larger but is first row
        else {
            return false;
        }
    }

    return false;
}

int main() {
    std::vector<std::vector<std::vector<int>>> cases = {
        {{1,3,5,7},{10,11,16,20},{23,30,34,60}}
    };

    std::vector<int> targets = {
        3, 
        13,
        0,
        1,
        10,
        23,
        5,
        7,
        11,
        16,
        20,
        30,
        34,
        60,
        2,
        9,
        12,
        21,
        100
    };

    std::vector<bool> expected = {
        true,  // 3
        false, // 13
        false, // 0
        true,  // 1
        true,  // 10
        true,  // 23
        true,  // 5
        true,  // 7
        true,  // 11
        true,  // 16
        true,  // 20
        true,  // 30
        true,  // 34
        true,  // 60
        false, // 2
        false, // 9
        false, // 12
        false, // 21
        false  // 100
        
    };

    for (unsigned i = 0; i < targets.size(); i++) {
        bool res = search(cases[0], targets[i]); 
        if (res == expected[i]) {
            std::cout << targets[i] << " Passed" << "\n";
        }
        else {
            std::cout << res << " expected " << expected[i] << " for target " << targets[i] << "\n";
        }
    }
    //search(cases[0], targets[11]);
}
