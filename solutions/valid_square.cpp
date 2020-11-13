#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

/*
 * Calculates distance between two points 
 */
float pointDistance(std::vector<int> &p1, std::vector<int> &p2) {
    int x1 = p1[0];
    int y1 = p1[1];
    int x2 = p2[0];
    int y2 = p2[1];
    
    return sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));
}

/*
 * Determines whether a set of 4 points creates a valid square
 */
bool validSquare(std::vector<int> &p1, std::vector<int> &p2, 
    std::vector<int> &p3, std::vector<int> &p4) {
    
    std::vector<float> distances;
    
    // Add all edges between p1 to other points
    distances.push_back(pointDistance(p1, p2));
    distances.push_back(pointDistance(p1, p3));
    distances.push_back(pointDistance(p1, p4));

    // All edges from p2 to other points
    distances.push_back(pointDistance(p2, p3));
    distances.push_back(pointDistance(p2, p4));

    // Edge from p3 to other points
    distances.push_back(pointDistance(p3, p4));

    // Sort them to separate square edges and diagonals
    std::sort(distances.begin(), distances.end());

    // Check that first four points are all the same
    for (unsigned i = 1; i < 4; i++) {
        if (distances[i] != distances[i - 1]) {
            return false;
        }
    }

    // Check that the diagonals are the same and the points aren't all the same
    if (distances[4] != distances[5] || (p1[0] == p2[0] && p1[1] == p2[1])) {
        return false;
    }

    return true;
}

int main() {
    std::vector<int> p1 = {1,0};
    std::vector<int> p2 = {0,1};
    std::vector<int> p3 = {0,-1};
    std::vector<int> p4 = {-11,0};

    std::cout << validSquare(p1, p2, p3 , p4) << "\n";
}
