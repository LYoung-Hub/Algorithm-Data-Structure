class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.split('-')

        ans = ''
        for st in s:
            ans = ans + st
        ans = ans.upper()

        curr = len(ans)
        while curr > K:
            ans = ans[:curr - K] + '-' + ans[curr - K:]
            curr -= K

        return ans
