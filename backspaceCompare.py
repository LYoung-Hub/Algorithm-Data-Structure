class Solution(object):

    def finalString(self, s):
        skip = 0
        curr = len(s) - 1
        ans = ''
        while curr >= 0:
            if s[curr] == '#':
                skip += 1
            else:
                if skip > 0:
                    skip -= 1
                else:
                    ans += s[curr]
            curr -= 1
        return ans

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if len(S) == 0 and len(T) == 0:
            return True

        final_s = self.finalString(S)
        final_t = self.finalString(T)

        return final_s == final_t
