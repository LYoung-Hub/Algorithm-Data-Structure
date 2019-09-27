class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        is_col = False
        for i in range(row):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(col):
                matrix[0][i] = 0

        if is_col:
            for i in range(row):
                matrix[i][0] = 0


if __name__ == '__main__':
    solu = Solution()
    solu.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
