from collections import Counter
import re


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        cnt = Counter(s)

        d = ['[']
        for key, value in cnt.items():
            if value < k:
                d.append(key)
        d.append(']')
        if len(d) == 2:
            return len(s)
        strs = re.split(r''.join(d), s)

        ans = 0
        for si in strs:
            if len(si) == 0:
                continue
            temp = self.longestSubstring(si, k)
            ans = max(ans, temp)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.longestSubstring("bbaaacbd", 3)
