class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        strs = str.split()
        if len(strs) == 0:
            return 0

        num = strs[0]
        ans = 0
        if ord('0') <= ord(num[0]) <= ord('9'):
            ans = self.convertPureNumber(num)
        if ord(num[0]) == ord('-'):
            ans = self.convertPureNumber(num[1:]) * -1
        if ord(num[0]) == ord('+'):
            ans = self.convertPureNumber(num[1:])

        low = pow(2, 31) * -1
        high = pow(2, 31) - 1

        if ans < low:
            return low
        if ans > high:
            return high

        return ans

    def convertPureNumber(self, str):
        idx = 0
        ans = 0
        while idx < len(str) and ord('0') <= ord(str[idx]) <= ord('9'):
            ans = ans * 10 + ord(str[idx]) - ord('0')
            idx += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.myAtoi('3.14')
