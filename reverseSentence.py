# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s) == 0:
            return ''
        strings = s.split(' ')
        length = len(strings)
        re = strings[length - 1]
        for i in range(length - 1, 0, -1):
            re = re + ' ' + strings[i - 1]
        return re
