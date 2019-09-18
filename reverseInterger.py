class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        while x % 10 == 0:
            x = x / 10

        ans = 0
        while x / 10 != 0:
            remainder = x % 10
            x = x / 10
            ans = ans * 10 + remainder

        ans = ans * 10 + x

        if pow(2, 31) * -1 < ans < pow(2, 31) - 1:
            return ans * sign

        return 0


if __name__ == '__main__':
    solu = Solution()
    print solu.reverse(-123)
