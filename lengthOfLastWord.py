class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0

        curr = length - 1
        ans = 0
        while curr >= 0:
            if ans > 0 and s[curr] == ' ':
                break
            if s[curr] != ' ':
                ans += 1
            curr -= 1

        return ans
