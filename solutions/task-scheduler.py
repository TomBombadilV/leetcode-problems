# Task Scheduler

from collections import Counter
from queue import PriorityQueue
from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    dic = Counter(tasks)
    pq = PriorityQueue()
    for key in dic:
        pq.put((dic[key], key))
    while not pq.empty():
        print(pq.get())
        
    
cases = [   (['A', 'A', 'A', 'B', 'B', 'B'], 2, 8),
            (['A', 'A', 'A', 'B', 'B', 'B'], 1, 6),
            (['A', 'A', 'A', 'B', 'C', 'C', 'C'], 3, 10),
            (['A', 'A', 'A', 'B', 'C', 'D', 'E'], 1, 7),
            (['A', 'A', 'A', 'B', 'C', 'D', 'E'], 0, 7)
]

for c in cases:
    t, n, a = c
    res = leastInterval(t, n)
    print("Passed" if res == a else "{0} failed {1} expected {2}".format(t, res, a))