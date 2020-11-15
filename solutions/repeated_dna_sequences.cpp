// Repeated DNA Sequences

#include <iostream>
#include <map>
#include <set>
#include <vector>

/*
 * Finds all repeated substrings of length 10.
 * Method copying set into vector.
 */
std::vector<std::string> search(std::string s) {
    std::set<std::string> set;
    std::set<std::string> res;

    if(s.size() < 10) {
        return {};
    }

    for (unsigned i = 0; i <= s.size() - 10; i++) {
        if (set.find(substring) != set.end()) {
            res.insert(substring);
        }
        else {
            set.insert(substring);
        }
    }
    
    std::vector<std::string> v(res.begin(), res.end());
    return v;
}

/*
 * Method map and vector
 */
std::vector<std::string> searchOld(std::string s) {
    std::map<std::string, int> dic;
    std::vector<std::string> res;

    for (unsigned i = 0; i <= s.size() - 10; i++) {
        std::string substring = s.substr(i, 10);
        if (dic.find(substring) != dic.end()) {
            if (dic[substring] == 1) {
                res.push_back(substring);
            }
            else {
                dic[substring]++;
            }
        }   
        else {
            dic[substring] = 1;
        }   
    }   

    return res;
}


int main() {
    std::vector<std::string> cases = {
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
        "",
        "A"
    };

    std::vector<std::vector<std::string>> expected = {
        {"AAAAACCCCC", "CCCCCAAAAA"},
        {"AAAAAAAAAA"},
        {},
        {}
    };

    for (unsigned i = 0; i < cases.size(); i++) {
        std::vector<std::string> res = search(cases[i]);
        if (res == expected[i]) {
            std::cout << "Passed" << "\n";
        }
        else {
            for (auto s : res) {
                std::cout << s << " ";
            }
            std::cout << "\n";
        }
    }
}
