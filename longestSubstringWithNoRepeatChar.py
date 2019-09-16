class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        ans = 0
        for i in range(0, len(s)):
            hash_set = {}
            max_len = 0
            j = i
            while j < len(s) and s[j] not in hash_set:
                hash_set[s[j]] = 1
                max_len += 1
                j += 1

            if max_len > ans:
                ans = max_len

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.lengthOfLongestSubstring('pwwkew')
