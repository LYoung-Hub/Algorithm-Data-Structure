class Solution(object):

    ans = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']

        self.ans = []
        self.backTracking(n, n, '')

        return self.ans

    def backTracking(self, left, right, comb):
        if left == 0 and right == 0:
            self.ans.append(comb)
            return

        if left == right:
            self.backTracking(left - 1, right, comb + '(')
        elif right > left > 0:
            self.backTracking(left - 1, right, comb + '(')
            self.backTracking(left, right - 1, comb + ')')
        elif left == 0 and right > 0:
            self.backTracking(0, right - 1, comb + ')')


if __name__ == '__main__':
    solu = Solution()
    print solu.generateParenthesis(3)
