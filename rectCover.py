# -*- coding:utf-8 -*-


class Solution:

    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number

        dp = [0, 1, 2]
        for i in range(3, number + 1):
            dp.append(dp[i - 2] + dp[i - 1])

        return dp.pop()
