// Longest Mountain in Array
#include <iostream>
#include <vector>

// Checks largest mountain surrounding given index
int maxMountain(std::vector<int>& arr, int i) {
    
    // Start mountain at given index
    int left = i;
    int right = i;

    // Find left bound of mountain side (decreasing from i to the left)
    while (left > 0 && arr[left - 1] < arr[left]) {
        left--;    
    }

    // Find right bound of mountain side (decreasing from i to the right)
    while (right < arr.size() - 1 && arr[right + 1] < arr[right]) {
        right++;
    }

    // Calculate size of mountain given left and right bounds
    int size = right - left + 1;

    // If size is smaller than 3, return 0
    return (left != i && right != i) ? size : 0;
}

// Finds the largest "mountain" in a given array
int findMountainOld(std::vector<int>& arr) {
    
    // Keep track of max mountain size calculated
    int max = 0;

    // Iterate through array and calculate largest mountain at each point
    for (unsigned i = 0; i < arr.size(); i++) {
        int currMax = maxMountain(arr, i);
        max = std::max(currMax, max);
    }

    return max;
}

int main() {
    std::vector<int> arr = {2,1,4,7,3,2,5};
    //arr = {2,2,2};
    //arr = {1,2,3,4,5,4};
    //arr = {};
    arr = {0,1,2,3,4,5,6,7,8,9};
    std::cout << findMountain(arr) << "\n"; 
}
