class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        if row == 0:
            return
        col = len(matrix[0])
        if col == 0:
            return
        self.dp = [[0 for j in range(col + 1)] for i in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.dp[i][col2 + 1] - self.dp[i][col1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    num_matrix = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    num_matrix.sumRegion(2, 1, 4, 3)
