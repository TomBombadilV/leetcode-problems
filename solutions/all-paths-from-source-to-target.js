// All Paths from Source to Target
// Modified DFS. Build current path using DFS, add to res if path ends at last node

const dfs = (graph, node, path, res) => {
    // Add current node to current path
    path.push(node);
    
    // If current node is also last node, add to path and stop recursing
    if (node == graph.length - 1) {
        res.push(path);
    } 
    // If not, perform DFS on all current node's neighbors
    else {
        for (let i = 0; i < graph[node].length; i++) {
            dfs(graph, graph[node][i], path.slice(0), res); // Use slice to create shallow copy
        }
    }
};

const allPathsSourceTarget = graph => {
    let res = [];
    dfs(graph, 0, [], res); 
    return res;
};

// Driver Code
let graph = [[1,2,3,4], [3], [3], [], [2]];
allPathsSourceTarget(graph);
