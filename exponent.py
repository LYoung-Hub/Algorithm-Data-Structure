# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0

        if exponent == 0:
            return 1
        elif exponent > 0:
            if exponent == 1:
                return base

            ans = 1
            while abs(exponent) > 1:
                remain = exponent % 2
                exponent = exponent / 2
                ans = ans * self.Power(base, exponent) * self.Power(base, exponent) * self.Power(base, remain)

            return ans
        else:
            exponent = abs(exponent)
            if exponent == 1:
                return base

            ans = 1
            while abs(exponent) > 1:
                remain = exponent % 2
                exponent = exponent / 2
                ans = ans * self.Power(base, exponent) * self.Power(base, exponent) * self.Power(base, remain)

            return 1.0 / ans


if __name__ == '__main__':
    solu = Solution()
    print solu.Power(2, -3)
