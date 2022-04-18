class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.stream = []

    def next(self, val: int) -> float:
        self.stream.append(val)
        n = len(self.stream)
        if n < self.size:
            return sum(self.stream)/n
        else:
            return sum(self.stream[-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
