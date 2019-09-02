# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0:
            return []

        ans = []
        for i in range(0, len(num) - size + 1):
            ans.append(max(num[i:(i + size)]))

        return ans
