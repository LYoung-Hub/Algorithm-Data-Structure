class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        left = 0
        right = len(A) - 1
        ans = -1
        while left < right:
            s = A[left] + A[right]
            if s < K:
                ans = max(ans, s)
                left += 1
            else:
                right -= 1

        return ans
