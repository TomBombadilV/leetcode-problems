#include <algorithm>
#include <iostream>
#include <vector>

void recurse(std::vector<int> &nums, 
    std::vector<int> curr, std::vector<std::vector<int>> &res) {
    // If no nums left to add, add curr to result 
    if (nums.size() == 0) {
        res.push_back(curr);
    }

    // Add each number to array and recurse
    for (unsigned i = 0; i < nums.size(); i++) {
        // Ignore instances where number has already been used
        if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
            // Create temporary array with current num
            std::vector<int> tempCurr = curr;
            tempCurr.push_back(nums[i]);
            // Create temporary nums excluding current num
            std::vector<int> tempNums = nums;
            tempNums.erase(tempNums.begin() + i);
            // Recurse with those
            recurse(tempNums, tempCurr, res);
        }
    }
}

std::vector<std::vector<int>> permuteUnique(std::vector<int> &nums) {
    // Sort nums so we can check if it is the same as previous number
    std::sort(nums.begin(), nums.end());

    std::vector<std::vector<int>> res;
    recurse(nums, {}, res);
    return res;
}

int main() {
    std::vector<int> nums = {};
    
    std::vector<std::vector<int>> res;
    res = permuteUnique(nums);

    for (unsigned i = 0; i < res.size(); i++) {
        for (unsigned j = 0; j < res[0].size(); j++) {
            std::cout << res[i][j] << " ";
        }
        std::cout << "\n";
    }
}
