# -*- coding:utf-8 -*-
class Solution:

    stack_data = []
    stack_min = []

    def push(self, node):
        # write code here
        self.stack_data.append(node)
        if not self.stack_min or self.stack_min[-1] > node:
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self):
        # write code here
        if self.stack_data is None:
            return None
        self.stack_min.pop()
        return self.stack_data.pop()

    def top(self):
        # write code here
        if self.stack_data is None:
            return None
        return self.stack_data[-1]

    def min(self):
        # write code here
        return self.stack_min[-1]
