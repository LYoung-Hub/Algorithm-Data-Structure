# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0

        ans = [0] * 32

        if n > 0:
            idx = 31
            while n > 0:
                ans[idx] = n % 2
                n = n / 2
                idx -= 1

            return sum(ans)
        elif n < 0:
            n = abs(n)
            idx = 31
            while n > 0:
                ans[idx] = n % 2
                n = n / 2
                idx -= 1

            ans.reverse()
            first_zero = ans.index(1)

            return 32 - sum(ans) - first_zero + 1


if __name__ == '__main__':
    solu = Solution()
    solu.NumberOf1(1)
