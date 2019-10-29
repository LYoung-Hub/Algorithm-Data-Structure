class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        idxs = []
        signs = []
        for i, ch in enumerate(S):
            if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
                stack.append(ch)
            else:
                signs.append(ch)
                idxs.append(i)
        ans = ''
        curr = 0
        id = 0
        while stack:
            if id < len(idxs) and curr == idxs[id]:
                ans += signs[id]
                id += 1
            else:
                ans += stack.pop()
            curr += 1
        while id < len(idxs):
            ans += signs[id]
            id += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.reverseOnlyLetters("ab-cd")
