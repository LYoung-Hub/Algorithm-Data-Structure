class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0

        ans = 0
        for i in range(0, length - 1):
            curr = ord(s[i]) - 64
            ans = pow(26, length - 1 - i) * curr + ans

        ans += ord(s[-1]) - 64

        return ans
