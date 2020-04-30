# LRU Cache
# Method 1:
# Use OrderedDict
# Method 2:
# Use dictionary and doubly linked list
# Time: O(1) | Space: O(n)

from collections import OrderedDict
from listnode import DoublyLinkedListNode

# Method 1
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity

    def put(self, key: int, value: int) -> None:
        # If key already in cache, reinsert it at the back
        if key in self.dic:
            del self.dic[key]
            self.dic[key] = value
        else:
            # If dictionary at capacity, evict least recently used (first in dic)
            if len(self.dic) == self.capacity:
                lru = next(iter(self.dic.items()))[0]
                del self.dic[lru]
            self.dic[key] = value

    def get(self, key: int) -> int:
        # If key exists, reinsert in back and return its value
        if key in self.dic:
            value = self.dic[key]
            del self.dic[key]
            self.dic[key] = value
            return value
        return -1

# Method 2
class LRUCache:
    def __init__(self, capacity: int):
        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        self.capacity = capacity

    # Insert node at tail
    def _insert_at_tail(self, ptr: DoublyLinkedListNode) -> None:
        self.tail.prev.next = ptr
        ptr.prev = self.tail.prev
        self.tail.prev = ptr
        ptr.next = self.tail

    # Remove node from old location
    def _remove_node(self, ptr: DoublyLinkedListNode) -> None:
        ptr.next.prev = ptr.prev
        ptr.prev.next = ptr.next
    
    def put(self, key: int, value: int) -> None:
        # If key already exists, reinsert node at tail
        if key in self.dic:
            ptr, value = self.dic[key]
            self._remove_node(ptr)
            self._insert_at_tail(ptr)
        else:
            # If at capacity, evict node at head (least recently used)
            if len(self.dic) == self.capacity:
                e_ptr = self.head.next
                e_key = e_ptr.val
                del self.dic[e_key]
                self._remove_node(e_ptr)
            # Add new node to dictionary and list
            ptr = DoublyLinkedListNode(key)
            self._insert_at_tail(ptr)
            self.dic[key] = (ptr, value)

    def get(self, key: int) -> int:
        # If key exists, reinsert at tail and get value
        if key in self.dic:
            ptr, value = self.dic[key]
            self._remove_node(ptr)
            self._insert_at_tail(ptr)
            return value
        return -1

# Driver Code
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
printList(cache.head)
cache.put(3, 3)
printList(cache.head)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
