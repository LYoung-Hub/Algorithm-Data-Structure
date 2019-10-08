class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_idx = {c: i for i, c in enumerate(S)}
        ans = []
        start = end = 0
        for i, c in enumerate(S):
            end = max(end, last_idx[c])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans
