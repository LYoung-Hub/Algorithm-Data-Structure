# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
        if len(s) == 0 or dic.count(s[0]) == 0:
            return 0
        for i in range(1, len(s)):
            if dic.count(s[i]) == 0:
                return 0
            elif dic.index(s[i]) == 10 or dic.index(s[i]) == 11:
                return 0

        if dic.index(s[0]) == 10 or dic.index(s[0]) == 11:
            ans = 0
            for i in range(1, len(s)):
                ans = dic.index(s[i]) + ans * 10
            if dic.index(s[0]) == 10:
                return ans * -1
            else:
                return ans
        else:
            ans = 0
            for i in range(0, len(s)):
                ans = dic.index(s[i]) + ans * 10
            return ans
