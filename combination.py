class Solution(object):

    ans = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == k:
            return []

        self.ans = []
        self.backTracking([], n, k)
        return self.ans

    def backTracking(self, comb, n, k):
        if k == 0:
            self.ans.append(comb)
            return

        for i in range(n, 0, -1):
            self.backTracking([i] + comb, i - 1, k - 1)


if __name__ == '__main__':
    solu = Solution()
    print solu.combine(4, 2)
