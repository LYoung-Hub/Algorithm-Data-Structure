class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt = []
        words = sorted(words, key=lambda x: len(x))
        for w in words:
            tmp = [0] * 26
            for ch in w:
                tmp[ord(ch) - ord('a')] += 1
            cnt.append(tmp)

        def isPredecessor(c1, c2):
            diff = 1
            for i, j in zip(c1, c2):
                if diff < 0 or i > j:
                    return False
                elif i < j:
                    diff -= j - i
            return diff == 0

        dp = [1] * len(cnt)
        ans = 1
        for i in range(1, len(cnt)):
            for j in xrange(i):
                if len(words[i]) - len(words[j]) == 1 and isPredecessor(cnt[j], cnt[i]):
                    dp[i] = max(dp[j] + 1, dp[i])
                    ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.longestStrChain(["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"])
