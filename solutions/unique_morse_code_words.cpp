// Unique Morse Code Words
#include <iostream>
#include <set>
#include <vector>

std::string morsify(std::string &word, std::vector<std::string> &dic) {
    
    std::string res = "";
    
    // Convert each char into morse representation, add to string representation
    for (char c : word) {
        int i = c - 'a';
        //std::cout << c << " " << i << " " << dic[i] << "\n";
        res += dic[i];
    }
    //std::cout << res << "\n";

    return res;
}

int morse(std::vector<std::string> &words) {
    
    // Define morse representation of each character (a = dic[0], 
    // b = dic[1], ... z = dic[25])
    std::vector<std::string> dic = { ".-","-...","-.-.","-..",".",
        "..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
        ".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
        "-.--","--.."
    };

    // Set so we get unique strings
    std::set<std::string> set;

    for (std::string word : words) {
        // Convert each word into morse and add to set
        set.insert(morsify(word, dic)); 
    }
    
    return set.size();
}

int main() {
    std::vector<std::vector<std::string>> cases = {
        {"gin", "zen", "gig", "msg"},
        {}
    };

    std::vector<int> expected = {
        2,
        0
    };

    for (unsigned i = 0; i < cases.size(); i++) {
        int res = morse(cases[i]);

        if (res == expected[i]) {
            std::cout << "Passed\n";
        }
        else {
            std::cout << res << " expected " << expected[i] << "\n";
        }
    }
}
