from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = right = 0
        curr = defaultdict(int)
        ans = 0
        while right < len(s):
            while right < len(s) and len(curr) <= k:
                curr[s[right]] += 1
                if len(curr) <= k:
                    ans = max(ans, right - left + 1)
                    right += 1
            while left <= right and len(curr) > k:
                if s[left] in curr:
                    curr[s[left]] -= 1
                    if curr[s[left]] == 0:
                        del curr[s[left]]
                left += 1
            right += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.lengthOfLongestSubstringKDistinct("eceba", 2)
