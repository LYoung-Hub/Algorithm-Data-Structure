class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1
        length = len(s)
        if length > 1:
            if s[1] == '0':
                if 0 < int(s[0:2]) <= 26:
                    dp[1] = 1
                else:
                    return 0
            else:
                if int(s[0:2]) <= 26:
                    dp[1] = 2
                else:
                    dp[1] = 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if 0 < int(s[i - 1:i + 1]) <= 26:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if s[i - 1] != '0':
                    if int(s[i - 1:i + 1]) <= 26:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1]

        return dp[-1]


if __name__ == '__main__':
    solu = Solution()
    print solu.numDecodings('101')
