class MaxStack(list):

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        """
        :rtype: int
        """
        return list.pop(self)[0]

    def top(self):
        """
        :rtype: int
        """
        return self[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        v = self[-1][1]
        temp = []
        while self[-1][0] != v:
            temp.append(self.pop())

        self.pop()
        while temp:
            self.push(temp.pop())
        return v

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
