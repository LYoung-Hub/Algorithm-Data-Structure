class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n != 0:
            n, remainder = divmod(n - 1, 26)
            ans = chr(65 + remainder) + ans
        return ans
