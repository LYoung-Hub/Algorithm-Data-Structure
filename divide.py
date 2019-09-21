class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        sign = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        quotient = self.division(dividend, divisor, 1)

        if sign:
            ans = quotient
        else:
            ans = 0 - quotient

        low = 0 - pow(2, 31)
        high = pow(2, 31) - 1
        if low <= ans <= high:
            return ans
        elif low > ans:
            return low
        else:
            return high

    def division(self, dividend, divisor, quotient):
        if dividend < divisor:
            return 0

        origin = divisor

        while dividend > divisor + divisor:
            divisor += divisor
            quotient += quotient

        if dividend > origin:
            quotient += self.division(dividend - divisor, origin, 1)

        return quotient


if __name__ == '__main__':
    solu = Solution()
    print solu.divide(-2147483648, -1)
