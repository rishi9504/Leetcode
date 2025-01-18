class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value = self.map[key]
        del self.map[key]
        self.map[key] = value
        return value

        

    def put(self, key: int, value: int) -> None:
        if key not in self.map and len(self.map) == self.capacity:
            del self.map[next(iter(self.map))]
        if key in self.map:
            del self.map[key]
        self.map[key]=value        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
