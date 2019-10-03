from collections import defaultdict


class TwoSum(object):

    nums = []
    hash_set = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.hash_set = defaultdict(list)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.nums.append(number)
        self.hash_set[number].append(len(self.nums) - 1)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if len(self.nums) < 2:
            return False

        for i in range(0, len(self.nums)):
            if (value - self.nums[i]) in self.hash_set:
                if (len(self.hash_set[value - self.nums[i]]) == 1 and i != self.hash_set[value - self.nums[i]][0]) or \
                        len(self.hash_set[value - self.nums[i]]) > 1:
                    return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)