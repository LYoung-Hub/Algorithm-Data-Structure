class Solution(object):

    ans = []

    def backTracking(self, s, n):
        if n == 0:
            self.ans.append(s)
            return

        if n == 1:
            half = len(s) / 2
            self.backTracking(s[:half] + '1' + s[half:], 0)
            self.backTracking(s[:half] + '8' + s[half:], 0)
            self.backTracking(s[:half] + '0' + s[half:], 0)

        if n > 1:
            if n > 3:
                self.backTracking('0' + s + '0', n - 2)

            self.backTracking('1' + s + '1', n - 2)
            self.backTracking('8' + s + '8', n - 2)
            self.backTracking('6' + s + '9', n - 2)
            self.backTracking('9' + s + '6', n - 2)

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        if n == 0:
            return self.ans

        self.backTracking('', n)

        return self.ans
