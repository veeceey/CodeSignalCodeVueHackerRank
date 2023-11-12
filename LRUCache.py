"""
Time complexity : \mathcal{O}(1)O(1) both for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done in a constant time.
Space complexity : \mathcal{O}(capacity)O(capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)
        ##pehlr add kar do phir zyada hoga to delete kareeinge

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
