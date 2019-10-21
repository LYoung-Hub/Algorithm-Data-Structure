class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        ans = [[0 for _ in xrange(row)] for _ in xrange(col)]
        for i in xrange(col):
            for j in xrange(row):
                ans[i][j] = A[j][i]
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.transpose([[1,2,3],[4,5,6]])
