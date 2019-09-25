class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            if all(i + k < len(s) and s[i + k] == x[k] for k in range(len(x))):
                s[i:i + len(x)] = y

        ans = ''
        return ans.join(s)
