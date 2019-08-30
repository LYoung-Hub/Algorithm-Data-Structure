# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number

        dp = [1, 2]
        for i in range(2, number):
            dp.append(sum(dp) + 1)

        return dp.pop()
