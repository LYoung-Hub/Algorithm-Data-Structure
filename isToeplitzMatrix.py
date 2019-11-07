class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        for i in xrange(row):
            r, c = row - i - 1, 0
            while r + 1 < row and c + 1 < col:
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
                r += 1
                c += 1
        for i in xrange(col):
            r, c = 0, i
            while r + 1 < row and c + 1 < col:
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
                r += 1
                c += 1
        return True


if __name__ == '__main__':
    solu = Solution()
    print solu.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
