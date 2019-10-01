class Solution(object):

    ans = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        self.backTracking(s, 3, '')
        return self.ans

    def backTracking(self, s, dots, comb):
        if len(s) == 0:
            return
        if dots == 0:
            if s[0] == '0' and len(s) > 1:
                return
            if 0 <= int(s) <= 255:
                self.ans.append(comb + s)
            return

        if s[0] == '0':
            self.backTracking(s[1:], dots - 1, comb + s[0] + '.')
            return

        for i in range(1, min(len(s), 3) + 1):
            if 0 <= int(s[:i]) <= 255:
                self.backTracking(s[i:], dots - 1, comb + s[:i] + '.')


if __name__ == '__main__':
    solu = Solution()
    print solu.restoreIpAddresses("010010")
