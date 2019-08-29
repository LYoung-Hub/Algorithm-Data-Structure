# -*- coding:utf-8 -*-
class Solution:

    stack_in = []
    stack_out = []

    def push(self, node):
        # write code here
        self.stack_in.append(node)

    def pop(self):
        # return xx
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
