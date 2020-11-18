// Merge Intervals
#include <algorithm>
#include <iostream>
#include <vector>

#include "print_vector.hpp"

// Returns 1 if a comes before b, else 0 
bool compare(std::vector<int>& a, std::vector<int>& b) {
    if (a[0] != b[0]) {
        return (a[0] < b[0]);
    }
    else {
        return (a[1] < b[1]);
    }
}

std::vector<std::vector<int>> merge(std::vector<std::vector<int>> intervals) {
    
    if (intervals.size() == 0 || intervals[0].size() == 0) {
        return intervals;
    }
    
    // Sort the intervals
    std::sort(intervals.begin(), intervals.end(), compare);

    std::vector<std::vector<int>> res;
    std::vector<int> curr = intervals[0];

    // Condense intervals
    for (std::vector<int> interval : intervals) {
        // If end of previous interval is greater than beginning of current
        // then there is overlap
        if (curr[1] >= interval[0]) {
            curr = {curr[0], std::max(curr[1], interval[1])};
        }
        // No overlap
        else {
            res.push_back(curr);
            curr = interval;
        }
    }
    // Add last interval
    res.push_back(curr);

    return res;
}

int main() {
    std::vector<std::vector<std::vector<int>>> cases = {
        {{8,10},{2,6},{15,18},{1,3}},
        {{1,4},{4,5}},
        {{}},
        {},
        {{1,3},{1,6}, {2,2}}
    };

    std::vector<std::vector<std::vector<int>>> expected = {
        {{1,6},{8,10},{15,18}},
        {{1,5}},
        {{}},
        {},
        {{1,6}}
    };

    for (unsigned i = 0; i < cases.size(); i++) {
        std::vector<std::vector<int>> res = merge(cases[i]);

        if (res == expected[i]) {
            std::cout << "Passed\n";
        }
        else {
            print2DVector(res);
            
            //std::cout << "Failed\n";
            //std::cout << res << " expected " << expected[i] << "\n";
        }
    }
}
