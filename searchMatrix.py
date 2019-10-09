class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False

        col = len(matrix[0])
        if col == 0:
            return False

        i = row - 1
        j = 0

        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1

        return False


if __name__ == '__main__':
    solu = Solution()
    print solu.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
