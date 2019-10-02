class Solution(object):

    memo = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.memo = {}
        return self.backTracking(s, wordDict, 0)

    def backTracking(self, s, word_dict, curr):
        length = len(s)
        if curr == length:
            return True

        if curr in self.memo:
            return self.memo[curr]

        for i in range(curr + 1, length + 1):
            if s[curr:i] in word_dict and self.backTracking(s, word_dict, i):
                self.memo[curr] = True
                return True

        self.memo[curr] = False
        return False


if __name__ == '__main__':
    solu = Solution()
    print solu.wordBreak('applepenapple', ['apple', 'pen'])
