# -*- coding:utf-8 -*-
# in progress
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None:
            return None

        row = len(matrix)
        col = len(matrix[0])

        if row == 1:
            return matrix[0]

        if col == 1:
            return [matrix[i][0] for i in range(0, row)]

        ans = []

        top = 0
        bottom = row - 1
        left = 0
        right = col - 1

        i = top
        j = left
        while left <= right and top <= bottom:
            i = top
            for j in range(left, right):
                ans.append(matrix[i][j])

            j = right
            for i in range(top, bottom):
                ans.append(matrix[i][j])

            i = bottom
            for j in range(right, left, -1):
                ans.append(matrix[i][j])

            j = left
            for i in range(bottom, top, -1):
                ans.append(matrix[i][j])
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if len(ans) < row * col:
            ans.append(matrix[top - 1][left - 1])

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.printMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
