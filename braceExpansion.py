class Solution(object):

    ans = []

    def backTracking(self, strs, s, length):
        if length == 0:
            self.ans.append(s)
            return

        for e in strs[0]:
            self.backTracking(strs[1:], s + e, length - 1)

    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)
        if length == 0:
            return []

        self.ans = []

        strs = []
        idx = 0
        while idx < length:
            if S[idx] == '{':
                idx += 1
                strs.append('')
                while S[idx] != '}':
                    if S[idx] != ',':
                        strs[-1] = strs[-1] + S[idx]
                    idx += 1
            else:
                strs.append(S[idx])
            idx += 1

        d_strs = []
        for string in strs:
            d_str = sorted(string)
            d_s = ''
            for e in d_str:
                d_s = d_s + e
            d_strs.append(d_s)

        self.backTracking(d_strs, '', len(d_strs))

        return self.ans


if __name__ == '__main__':
    solu = Solution()
    print solu.expand("{a,b}c{d,e}f")
