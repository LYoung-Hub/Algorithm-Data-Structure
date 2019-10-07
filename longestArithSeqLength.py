from collections import defaultdict


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ans = 1
        for i in range(0, len(A)):
            for j in range(i):
                v = A[i] - A[j]
                d[(i, v)] = max(d[(j, v)] + 1, d[(i, v)])
                ans = max(d[(i, v)], ans)
        return ans + 1
