//
#include <iostream>
#include <vector>

int main() {
    std::vector< > cases = {
    };

    std::vector< > expected = {
    };

    for (unsigned i = 0; i < cases.size(); i++) {
        _ res = _(cases[i]);

        if (res == expected[i]) {
            std::cout << "Passed\n";
        }
        else {
            std::cout << res << " expected " << expected[i] << "\n";
        }
    }
}
