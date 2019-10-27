class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if i == 0:
                    ans += grid[i][j]
                else:
                    ans += max(0, grid[i][j] - grid[i - 1][j])

                if j == 0:
                    ans += grid[i][j]
                else:
                    ans += max(0, grid[i][j] - grid[i][j - 1])

                if i == len(grid) - 1:
                    ans += grid[i][j]
                else:
                    ans += max(0, grid[i][j] - grid[i + 1][j])

                if j == len(grid[0]) - 1:
                    ans += grid[i][j]
                else:
                    ans += max(0, grid[i][j] - grid[i][j + 1])

                if grid[i][j] > 0:
                    ans += 2
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.surfaceArea([[1,0],[0,2]])
