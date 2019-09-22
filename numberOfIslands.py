class Solution(object):

    def DFS(self, grid, row, column):
        r = len(grid)
        c = len(grid[0])

        if row < 0 or column < 0 or row > r - 1 or column > c - 1 or grid[row][column] == '0':
            return

        grid[row][column] = '0'
        self.DFS(grid, row + 1, column)
        self.DFS(grid, row - 1, column)
        self.DFS(grid, row, column + 1)
        self.DFS(grid, row, column - 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        row = len(grid)
        if row == 0:
            return ans
        column = len(grid[0])
        if column == 0:
            return ans

        for i in range(0, row):
            for j in range(0, column):
                if grid[i][j] == '1':
                    ans += 1
                    self.DFS(grid, i, j)

        return ans
