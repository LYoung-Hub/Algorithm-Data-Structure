# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        curr = 0
        for i in range(0, len(pushV)):
            if pushV[i] != popV[curr]:
                stack.append(pushV[i])
            else:
                curr += 1

        while stack:
            top = stack.pop()
            if top != popV[curr]:
                return False
            else:
                curr += 1

        return True


if __name__ == '__main__':
    solu = Solution()
    solu.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
