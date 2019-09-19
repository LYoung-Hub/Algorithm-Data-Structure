class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        model = strs[0]
        idx = 0
        common_prefix = ''
        while idx < len(model):
            for i in range(1, len(strs)):
                if idx == len(strs[i]) or strs[i][idx] != model[idx]:
                    return common_prefix
            common_prefix += model[idx]
            idx += 1

        return common_prefix
