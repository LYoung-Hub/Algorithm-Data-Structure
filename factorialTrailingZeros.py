class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        five_count = 0
        i = 5
        while i <= n:
            five_count += n / i
            i = i * 5
        return five_count
