// Minimum Number of Vertices to Reach All Nodes
// Keep track of all nodes that have no edges leading to them

const test = require('./test');

const findSmallestSetOfVertices = (n, edges) => {
    let set = new Set();
    // Add all vertices to set
    for (let i = 0; i < n; i++) {
        set.add(i);
    }
    // Delete all vertices with incoming edge from set
    edges.forEach(edge => {
        set.delete(edge[1]);
    });
    // Return list of all vertices with no incoming edges
    return [...set];
};

const cases = [
    [6, [[0,1],[0,2],[2,5],[3,4],[4,2]], [0, 3]],
    [5, [[0,1],[2,1],[3,1],[1,4],[2,4]], [0, 2, 3]]
];

test(cases, findSmallestSetOfVertices);
