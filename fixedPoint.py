class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        mid = left + (right - left) / 2
        while left < right:
            if A[mid] < mid:
                left = mid + 1
            else:
                right = mid
            mid = left + (right - left) / 2
        return left if A[left] == left else -1
