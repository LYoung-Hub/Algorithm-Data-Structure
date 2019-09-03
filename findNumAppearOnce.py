# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        hash_set = {}
        for i in range(0, len(array)):
            if array[i] not in hash_set:
                hash_set[array[i]] = 1
                continue
            if array[i] in hash_set:
                del hash_set[array[i]]

        return hash_set.keys()


if __name__ == '__main__':
    solu = Solution()
    solu.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5])
