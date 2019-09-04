# -*- coding:utf-8 -*-
# 二分查找，自测通过，提交超时
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0

        left = 0
        right = len(data) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) / 2
            if data[mid] == k:
                break
            elif data[mid] < k:
                left = mid
            elif data[mid] > k:
                right = mid

        if data[mid] != k:
            return 0

        i = mid
        while i > 0 and data[i] == data[i - 1]:
            i -= 1

        j = mid
        while j < (len(data) - 1) and data[j] == data[j + 1]:
            j += 1

        return j - i + 1


if __name__ == '__main__':
    solu = Solution()
    solu.GetNumberOfK([1, 2, 3, 3, 3, 4], 3)
