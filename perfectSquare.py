class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [float('Inf')] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(n**0.5) + 1)) + 1
        return dp[-1]
