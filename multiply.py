# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        dp_head = [A[0]]
        dp_tail = [A[length - 1]]
        for i in range(1, length - 1):
            dp_head.append(dp_head[i - 1] * A[i])
            dp_tail.append(dp_tail[i - 1] * A[length - 1 - i])

        dp_tail.reverse()
        B = [dp_tail[0]]
        for i in range(1, len(A) - 1):
            B.append(dp_head[i - 1] * dp_tail[i])
        B.append(dp_head[-1])

        return B


if __name__ == '__main__':
    solu = Solution()
    print solu.multiply([1, 2, 3, 4, 5])
