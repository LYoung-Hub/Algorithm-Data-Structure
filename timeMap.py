from collections import defaultdict


class TimeMap(object):

    hash_set = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hash_set[key].append([value, timestamp])
        sorted(self.hash_set[key])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        length = len(self.hash_set[key])
        if length == 0:
            return ''
        else:
            if timestamp < self.hash_set[key][0][1]:
                return ''
            if timestamp >= self.hash_set[key][-1][1]:
                return self.hash_set[key][-1][0]
            idx = self.binarySearch(self.hash_set[key], timestamp)
            return self.hash_set[key][idx][0]

    def binarySearch(self, l, timestamp):
        left = 0
        right = len(l) - 1
        mid = left + (right - left) / 2
        while left < right:
            if l[mid][1] <= timestamp < l[mid + 1][1]:
                return mid
            elif timestamp < l[mid][1]:
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) / 2
        return left


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
