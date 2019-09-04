# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        great_sum = array[0]
        curr_sum = array[0]
        for i in range(1, len(array)):
            if curr_sum < 0:
                curr_sum = array[i]
            else:
                curr_sum += array[i]

            if curr_sum > great_sum:
                great_sum = curr_sum

        return great_sum
