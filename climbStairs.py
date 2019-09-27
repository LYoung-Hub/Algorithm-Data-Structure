class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2]

        curr = 2
        while curr < n:
            dp.append(dp[curr - 1] + dp[curr - 2])
            curr += 1

        return dp[n - 1]
