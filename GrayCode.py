class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        dp = [0]
        head = 1
        for i in range(n):
            for j in range(len(dp) - 1, -1, -1):
                dp.append(head + dp[j])
            head = head << 1
        return dp
