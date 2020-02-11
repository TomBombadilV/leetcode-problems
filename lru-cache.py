# Least Recently Used Cache
# Use OrderedDict
# Time: O(1) | Space: O(n)

from collections import OrderedDict

class LRUCache:
    key_dict = OrderedDict()
    capacity = None

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If key exists, pop it and put it back in to bump it to the front
        if key in self.key_dict:
            val = self.key_dict.pop(key)
            self.key_dict[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        # If cache is full, remove the least recently used item
        if len(self.key_dict) == self.capacity:
            self.key_dict.pop(list(self.key_dict.items())[0][0])
        # Add new item
        self.key_dict[key] = value

commands = ["LRUCache","put","get","put","get","get"]
inputs = [[1],[2,1],[2],[3,2],[2],[3]]
cache = LRUCache(1)
cache.put(2, 1)
print(cache.get(2))
cache.put(3,2)
print(cache.get(2))
print(cache.get(3))