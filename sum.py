# -*- coding:utf-8 -*-
class Solution:

    ans = 0

    def sum(self, n):
        self.ans += n - 1
        n -= 1
        n and self.sum(n)

    def Sum_Solution(self, n):
        # write code here
        self.ans = n
        self.ans and self.sum(n)
        return self.ans


if __name__ == '__main__':
    solu = Solution()
    solu.Sum_Solution(1)
