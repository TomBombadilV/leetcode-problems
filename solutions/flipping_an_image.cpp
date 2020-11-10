#include <iostream>
#include <vector>

void flipSwap(std::vector<std::vector<int>> &m, int i, int j, int rowSize, int half) {
    // Check that indices are valid
    if (i < 0 || i >= m.size() || j < 0 || (m.size() > 0 && j >= m[0].size())) {
        return;
    }

    // Get left and right values to be swapped
    int left = m[i][j];
    int right = m[i][rowSize - j - 1];

    // Flip those values from 1 to 0 or 0 to 1
    left = 1 - left;
    right = 1 - right;

    // Assign values to swapped locations
    m[i][j] = right;
    m[i][rowSize - j - 1] = left;
}

std::vector<std::vector<int>> flipMatrix(std::vector<std::vector<int>> &m) {
    
    if (m.size() < 1) {
        return m;
    }

    // Calculate size and midpoint of matrix rows
    int rowSize = m[0].size();
    int half = (rowSize + 1) / 2; // Ceiling division so that middle cell is flipped

    // Iterate through each row of the matrix
    for (unsigned i = 0; i < m.size(); i++) {
        // Perform a swap on the first half of the array
        for (unsigned j = 0; j < half; j++) {
            // Flip and swap current index and its complement
            flipSwap(m, i, j, rowSize, half);
        }
    }

    return m;
}

int main() {
    
    //std::vector<std::vector<int>> test = {{1,1,0},{1,0,1},{0,0,0}};
    std::vector<std::vector<int>> test = {{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}};
    //std::vector<std::vector<int>> test = {{}};

    flipMatrix(test);

    if (test.size() < 1) {
        std::cout << "\n";
    }
    else {
        for (unsigned i = 0; i < test.size(); i++) { 
            for (unsigned j = 0; j < test[0].size(); j++) {
                std::cout << test[i][j] << " ";
            }
            std:: cout << "\n";
        }
    }
}
