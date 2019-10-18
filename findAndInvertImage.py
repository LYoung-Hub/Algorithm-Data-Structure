class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            self.helper(row)
        return A

    def helper(self, row):
        left = 0
        right = len(row) - 1
        while left < right:
            if row[left] == row[right]:
                row[left] = 1 if row[left] == 0 else 0
                row[right] = 1 if row[right] == 0 else 0
            left += 1
            right -= 1
        if left == right:
            row[left] = 1 if row[left] == 0 else 0


if __name__ == '__main__':
    solu = Solution()
    print solu.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
