// Useful functions for vectors

#include <iostream>
#include <vector>

#include "print_vector.hpp"

/* 
 * Prints out the elements of a 1-D vector in one line.
 */
template <typename T> 
void print1DVector(std::vector<T> &v) {
        
    // Print each element of vector
    for (unsigned i = 0; i < v.size(); i++) {
        std::cout << v[i] << " ";
    }   

    std::cout << "\n";
}

// Link 'em via explicit instantiation
template void print1DVector<int>(std::vector<int> &v);
template void print1DVector<std::string>(std::vector<std::string> &v);

/*
 * Prints out the elements of a 2-D vector.
 */
template <typename T> 
void print2DVector(std::vector<std::vector<T>> &v) {

    for (unsigned i = 0; i < v.size(); i++) {
        for (unsigned j = 0; j < v[0].size(); j++) {
            std::cout << v[i][j] << " ";
        }
        std:: cout << "\n";
    }
    std::cout << "\n";
}

// Link 'em via explicit instantiation
template void print2DVector<int>(std::vector<std::vector<int>> &v);
template void print2DVector<std::string>(std::vector<std::vector<std::string>> &v);
