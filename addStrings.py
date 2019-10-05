class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)

        idx1 = length1 - 1
        idx2 = length2 - 1

        ans = ''
        c = 0
        while idx1 >= 0 and idx2 >= 0:
            curr = (int(num1[idx1]) + int(num2[idx2]) + c) % 10
            c = (int(num1[idx1]) + int(num2[idx2]) + c) / 10
            ans = str(curr) + ans
            idx1 -= 1
            idx2 -= 1

        while idx1 >= 0:
            curr = (int(num1[idx1]) + c) % 10
            c = (int(num1[idx1]) + c) / 10
            ans = str(curr) + ans
            idx1 -= 1

        while idx2 >= 0:
            curr = (int(num2[idx2]) + c) % 10
            c = (int(num2[idx2]) + c) / 10
            ans = str(curr) + ans
            idx2 -= 1

        if c:
            ans = str(c) + ans
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.addStrings('1', '1')
