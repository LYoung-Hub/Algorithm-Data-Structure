class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ref = [0] * 26
        curr = [0] * 26
        for item in p:
            ref[ord(item) - 97] += 1
        idx = 0
        ans = []
        length = len(p)
        while idx < len(s):
            curr[ord(s[idx]) - 97] += 1
            if curr == ref:
                ans.append(idx + 1 - length)
            if idx + 1 - length >= 0:
                curr[ord(s[idx + 1 - length]) - 97] -= 1
            idx += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.findAnagrams("baa", "aa")
