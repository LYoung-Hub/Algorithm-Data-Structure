from collections import deque


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        s = s.upper()
        for i in range(0, len(s)):
            if 65 <= ord(s[i]) <= 90 or 48 <= ord(s[i]) <= 57:
                q.append(s[i])

        while q:
            if len(q) == 1:
                return True
            if q.popleft() != q.pop():
                return False

        return True


if __name__ == '__main__':
    solu = Solution()
    print solu.isPalindrome("`l;`` 1o1 ??;l`")
