class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least
        
        self.cache = {}
        self.nodes = 0

    def remove(self, key: int) -> None:
        p = self.cache[key]
        self.cache.pop(key, None)
        p.prev.next = p.next
        p.next.prev = p.prev
        p.next = p.prev = None
        self.nodes -= 1
    
    def add(self, key: int, value: int) -> None:
        p = Node(key, value)
        p.prev, p.next = self.most.prev, self.most
        self.most.prev.next = p
        self.most.prev = p
        self.cache[key] = p
        self.nodes += 1
    
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val
            self.remove(key)
            self.add(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        if self.nodes >= self.capacity:
            self.remove(self.least.next.key)
        self.add(key, value)
