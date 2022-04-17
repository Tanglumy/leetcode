class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.x = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.x:
            return False
        else:
            self.nums.append(val)
            self.x[val] = len(self.nums)-1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.x:
            return False
        else:
            index = self.x[val]
            # print(index,self.nums)
            self.nums[index] = self.nums[-1]
            self.x[self.nums[-1]] = index
            self.nums.pop()
            self.x.pop(val)
            # print(index,self.x)

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # print(self.nums)
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
