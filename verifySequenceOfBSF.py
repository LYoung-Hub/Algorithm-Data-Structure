# -*- coding:utf-8 -*-

class Solution:

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        if len(sequence) == 1 or len(sequence) == 2:
            return True

        root = sequence[-1]
        idx = -1
        for i in range(len(sequence) - 1, -1, -1):
            if sequence[i] < root:
                idx = i
                break

        for i in range(0, idx):
            if sequence[i] > root:
                return False

        left = True
        right = True
        if idx >= 0:
            left = self.VerifySquenceOfBST(sequence[0:(idx + 1)])
        if idx < len(sequence) - 2:
            right = self.VerifySquenceOfBST(sequence[(idx + 1): (len(sequence) - 1)])

        return left and right


if __name__ == '__main__':
    solu = Solution()
    solu.VerifySquenceOfBST([7, 4, 6, 5])
