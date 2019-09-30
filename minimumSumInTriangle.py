class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        dp = [[0] * len(triangle[-1]) for i in range(row)]
        dp[0][0] = triangle[0][0]

        for i in range(1, row):
            for j in range(0, i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:
                    if i == j:
                        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[-1])


if __name__ == '__main__':
    solu = Solution()
    print solu.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
