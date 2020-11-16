// DFS and BFS with Matrix Representation
#include <iostream>
#include <queue>
#include <vector>

void dfs(std::vector<std::vector<int>> &g, int v, std::vector<bool> &visited) {
    visited[v] = true;
    std::cout << v << " ";
    for (unsigned i = 0; i < g.size(); i++) {
        if (!visited[i] && g[v][i]) {
            dfs(g, i, visited);
        }
    }
}

void connected(std::vector<std::vector<int>> &g) {
    std::cout << "Connected components -\n";
    
    std::vector<bool> visited(g.size());

    for (unsigned v = 0; v < g.size(); v++) {
        if (!visited[v]) {
            dfs(g, v, visited);
            std::cout << "\n";
        }
    }
}

void bfs(std::vector<std::vector<int>> &g) {
    for (int v = 0; v < g.size(); v++) {
        
        std::cout << "BFS from vertex " << v << "\n";

        std::vector<bool> visited(g.size());

        std::queue<std::vector<int>> q;
        q.push({v, 0});
        visited[v] = true;

        int prevLevel = 0;

        std::cout << "Level 0: ";

        while (!q.empty()) {
            std::vector<int> curr = q.front();
            q.pop();

            int currV = curr[0];
            int currLevel = curr[1];

            if (currLevel != prevLevel) {
                std::cout << "\n";
                std::cout << "Level " << currLevel << ": ";
            }
            
            std::cout << currV << " ";
            
            prevLevel = currLevel;
            
            for (int i = 0; i < g.size(); i++) {
                if (!visited[i] && g[currV][i]) {
                    q.push({i, currLevel + 1});
                    visited[i] = true;
                }
            }
        }

        std::cout << "\n";
    }
}

int main() {
    std::vector<std::vector<int>> g = {
       //0  1  2  3  4  5
        {0, 0, 0, 1, 0, 1}, //0
        {0, 0, 1, 0, 0, 0}, //1
        {0, 1, 0, 0, 0, 0}, //2
        {1, 0, 0, 0, 1, 1}, //3
        {0, 0, 0, 1, 0, 0}, //4
        {1, 0, 0, 1, 0, 0}  //5
    };

    connected(g);

    bfs(g);
}
