class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > mask else a


if __name__ == '__main__':
    solu = Solution()
    print solu.getSum(-12, -8)
