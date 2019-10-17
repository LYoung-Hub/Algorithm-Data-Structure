from collections import deque


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.q = deque([])
        for i in v:
            self.q.extend(i)

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
