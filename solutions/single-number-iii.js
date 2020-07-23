// Single Number III
// Method 1: Count the frequency of each number using a dictionary | Space: O(n)
// Method 2: Use a set and delete if curr num exists in set | Space: O(n)
// Method 3: Sort and check | Time: O(nlogn)
// Method 4: XOR wot?

const singleNumber = nums => {
    // Get two unique numbers xor-ed together
    let xor = 0;
    for (let i = 0; i < nums.length; i++) {
        xor ^= nums[i];
    }

    // Get most significant set bit
    const setBit = xor & -xor;

    // Partition xor by set bit
    let xorA = 0;
    let xorB = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] & setBit) xorA ^= nums[i];
        else xorB ^= nums[i];
    }
    return [xorA, xorB];
};

// Driver Code
const nums = [-1, 2, -3, -2, -1, 2]
console.log(singleNumber(nums));
