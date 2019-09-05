# -*- coding:utf-8 -*-
# 分治、归并
class Solution:

    def InversePairs(self, data):
        # write code here
        if len(data) == 0:
            return 0

        def mergeSort(data, begin, end):
            if begin == end - 1:
                return 0
            mid = int((begin + end) / 2)
            left_count = mergeSort(data, begin, mid)
            right_count = mergeSort(data, mid, end)
            merge_count = merge(data, begin, mid, end)
            return left_count + right_count + merge_count

        def merge(data, begin, mid, end):
            i = begin
            j = mid
            count = 0
            temp = []
            while i < mid and j < end:
                if data[i] <= data[j]:
                    temp.append(data[i])
                    i += 1
                else:
                    temp.append(data[j])
                    j += 1
                    count += mid - i
            while i < mid:
                temp.append(data[i])
                i += 1
            while j < end:
                temp.append(data[j])
                j += 1
            data[begin: end] = temp
            del temp
            return count

        begin = 0
        end = len(data)
        ans = mergeSort(data, begin, end)
        return ans % 1000000007
