import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = {}
        self.values = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash_set:
            self.hash_set[val] = self.length
            self.values.append(val)
            self.length += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash_set:
            return False
        else:
            self.hash_set[self.values[-1]] = self.hash_set[val]
            self.values[self.hash_set.pop(val)] = self.values[-1]
            self.values.pop()
            self.length -= 1
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randint(0, self.length - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
