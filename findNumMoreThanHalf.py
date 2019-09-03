# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if length == 0:
            return 0
        if length == 1:
            return numbers[0]
        hash_set = {}
        for i in range(0, length):
            if numbers[i] not in hash_set:
                hash_set[numbers[i]] = 1
                continue
            if numbers[i] in hash_set:
                if hash_set[numbers[i]] == length / 2:
                    return numbers[i]
                else:
                    hash_set[numbers[i]] += 1

        return 0
