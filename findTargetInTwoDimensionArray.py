# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row_len = len(array)
        col_len = len(array[0])
        if row_len == 0 or col_len == 0:
            return False

        if target < array[0][0] or target > array[row_len - 1][col_len - 1]:
            return False

        i = row_len - 1
        j = 0
        while i >= 0 and j <= col_len - 1:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1

        return False
