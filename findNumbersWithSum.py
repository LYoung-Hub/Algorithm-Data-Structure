# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ans = []
        for i in range(0, len(array)):
            if array[i] > tsum:
                break
            if array.count(tsum - array[i]) > 0:
                ans.append([array[i], tsum - array[i]])

        if len(ans) == 0:
            return ans

        min_mul = tsum * tsum
        min_idx = -1
        for i in range(0, len(ans)):
            mul = ans[i][0] * ans[i][1]
            if min_mul > mul:
                min_mul = mul
                min_idx = i

        return ans[min_idx]


if __name__ == '__main__':
    solu = Solution()
    solu.FindNumbersWithSum([1, 2, 4, 7, 11, 16], 10)
