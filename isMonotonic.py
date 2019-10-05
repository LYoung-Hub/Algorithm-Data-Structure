class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = decrease = True
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                increase = False
            if A[i] < A[i + 1]:
                decrease = False
        return increase or decrease
