# Last Stone Weight
# Three methods: 
# 1. Keep taking a diff array until 1 number is left O(n(n-1)/2) => O(n^2)
# 2. Sort the array and keep it sorted, diffing the largest two numbers and
#    reinserting the resulting number into the sorted array until one number
#    is left O(nlogn)
# 3. Use a priority queue O(nlogn)

from bisect import insort
from typing import List
from queue import PriorityQueue

# Method #1
def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) > 1:
        diff = []
        for i in range(len(stones) - 1):
            diff.append(stones[i + 1] - stones[i])
        stones = diff
    return stones[0]

# Method #2
def lastStoneWeight(stones: List[int]) -> int:
    # Sort list in nlogn time
    stones = sorted(stones)
    while len(stones) > 1:
        diff = stones[-1] - stones[-2]
        stones = stones[:-2]
        # Insert into list in logn time using binary search. 
        # Unfortunately, insort is O(n)
        insort(stones, diff)
    return stones[0]

# Method #3
def lastStoneWeight(stones: List[int]) -> int:
    # Insert stones into priority queue
    q = PriorityQueue()
    for stone in stones:
        # We want max queue, but Python priority queue is a min queue, so 
        # negate stone weight
        q.put(-stone)
    while q.qsize() > 1:
        a, b = -q.get(), -q.get()
        diff = a - b
        q.put(-diff)
    return -q.get()

# Driver code
cases = [   [2, 7, 4, 1, 8, 1],
            [2, 10, 50, 11, 101, 102]
]

for case in cases:
    print(lastStoneWeight_2(case), lastStoneWeight(case))
