class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j - 1 >= 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]

        return dp[m - 1][n - 1]
