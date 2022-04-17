class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.temp = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.temp:
            self.queue.remove(key)
            self.queue.append(key)
            return self.temp[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.temp:
            self.temp[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        elif key not in self.temp and len(self.temp) == self.capacity:
            self.temp.pop(self.queue.pop(0))
            self.temp[key] = value
            self.queue.append(key)
        else:
            self.temp[key] = value
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
