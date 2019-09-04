# -*- coding:utf-8 -*-
# in progress
import math


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 0:
            return 0

        if 0 < n < 10:
            return 1

        ans = 0
        while n >= 100:
            log = int(math.log(n, 10))
            n = n - pow(10, log) + 1
            ans = ans + log * pow(10, log - 1) + n

        if n / 10 == 1:
            ans = ans + 2 + n % 10
        if n / 10 > 1:
            if n % 10 >= 1:
                ans = ans + 12 + (n / 10) - 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    solu.NumberOf1Between1AndN_Solution(21345)
