# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 2:
            return number

        dp = [1, 2]
        for i in range(2, number):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp.pop()
