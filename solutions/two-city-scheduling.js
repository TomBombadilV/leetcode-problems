// Two City Scheduling

const twoCitySchedCost = costs => {
    // Calculate each person's cost difference. Save array of [difference, city A cost]
    costs = costs.map(cost => [cost[0] - cost[1], cost[0]]);
    // Sort by difference
    costs.sort((costA, costB) => costA[0] < costB[0] ? -1 : 0);
    // Calculate how many people in each city
    let N = costs.length / 2;
    // Add city A cost for first N people, then add city A cost minus difference for second half
    let min = costs.reduce((sum, cost, i) => {
        if (i < N) {
            return sum + cost[1];
        }
        else {
            return sum + cost[1] - cost[0];
        }
    }, 0);
    return min;
};

let costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
twoCitySchedCost(costs);
