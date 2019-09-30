class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        stack = [[1], [1, 1]]

        for i in range(2, numRows):
            stack.append([1])
            for j in range(0, len(stack[i - 1]) - 1):
                stack[i].append(stack[i - 1][j] + stack[i - 1][j + 1])
            stack[i].append(1)

        return stack[numRows]
