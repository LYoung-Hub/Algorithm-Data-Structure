class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        row = []
        col = []
        for r in grid:
            row.append(max(r))
        for i in xrange(cols):
            temp = [r[i] for r in grid]
            col.append(max(temp))
        ans = 0
        for i in xrange(rows):
            for j in xrange(cols):
                target = min(row[i], col[j])
                ans += max(0, target - grid[i][j])
        return ans
