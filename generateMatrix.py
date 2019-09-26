class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        row = n
        col = n

        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)

        top = 0
        bottom = row - 1
        left = 0
        right = col - 1

        element = 1
        while left <= right and top <= bottom:
            i = top
            for j in range(left, right + 1):
                matrix[i][j] = element
                element += 1

            j = right
            for i in range(top + 1, bottom + 1):
                matrix[i][j] = element
                element += 1

            if top < bottom and left < right:
                i = bottom
                for j in range(right - 1, left, -1):
                    matrix[i][j] = element
                    element += 1

                j = left
                for i in range(bottom, top, -1):
                    matrix[i][j] = element
                    element += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix


if __name__ == '__main__':
    solu = Solution()
    print solu.generateMatrix(3)
