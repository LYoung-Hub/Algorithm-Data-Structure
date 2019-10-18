class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        curr = 0
        length = len(S)
        strs = []
        while curr < length:
            temp = S[curr]
            while curr < length - 1 and S[curr] == S[curr + 1]:
                curr += 1
                temp += S[curr]
            if temp != '':
                strs.append(temp)
            curr += 1
        ans = 0
        for s in strs:
            l = len(s)
            ans += l * (l + 1) / 2
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.countLetters("aaaba")
