class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return None

        row = len(matrix)
        if row == 0:
            return []

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

        while left <= right and top <= bottom:
            i = top
            for j in range(left, right + 1):
                ans.append(matrix[i][j])

            j = right
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][j])

            if top < bottom and left < right:
                i = bottom
                for j in range(right - 1, left, -1):
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
