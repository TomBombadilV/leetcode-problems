// Redundant Connection
#include <iostream>
#include <stack>
#include <vector>

std::vector<int> dfs(std::vector<std::vector<int>> g) {
    std::vector<bool> visited(g.size());

    std::stack<int> s;
    s.push(0);
    visited[0] = true;

    while (!s.empty()) {
        int v = s.top();
        s.pop();

        std::cout << "Searching vertex " << v << "\n";

        for (unsigned i = 0; i < g[v].size(); i++) {
            int tail = g[v][i];
            // If tail vertex has been visited already, return edge leading to it
            if (visited[tail]) {
                std::cout << "found cycle\n";
                return {v, tail};
            }
            else {
                s.push(tail);
                visited[tail] = true;
            }
        }
    }

    std::cout << "No cycle detected.\n"; 
    return {-1, -1};
}


std::vector<int> findRedundantConnection(std::vector<std::vector<int>> &edges) {
    
    std::vector<std::vector<int>> adjacencyList(edges.size());
    
    // Parse edges into an adjacency matrix for faster lookups
    for (unsigned i = 0; i < edges.size(); i++) {
        std::vector<int> edge = edges[i];
        adjacencyList[edge[0] - 1].push_back(edge[1] - 1);
    }

    std::vector<bool> visited(edges.size());
    
    return dfs(adjacencyList);
    
}

int main() {
    std::vector<std::vector<int>> edges = {{1,2}, {1,3}, {2,3}};
    //edges = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};

    std::vector<int> res = findRedundantConnection(edges);

    for (unsigned i = 0; i < res.size(); i++) {
        std::cout << res[i] << " ";
    }
    std::cout << "\n";
}   
