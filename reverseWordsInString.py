class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return ''
        stack = []
        idx = 0
        while idx < length:
            while idx < length and s[idx] == ' ':
                idx += 1
            curr = ''
            while idx < length and s[idx] != ' ':
                curr += s[idx]
                idx += 1
            if curr != '':
                stack.append(curr)

        ans = ''
        while stack:
            ans += stack.pop() + ' '
        return ans[:-1]


if __name__ == '__main__':
    solu = Solution()
    print solu.reverseWords("  hello world!  ")
