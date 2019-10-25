class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        curr = len(A) - 1
        while curr - 2 >= 0:
            if A[curr - 2] + A[curr - 1] <= A[curr]:
                curr -= 1
            else:
                return A[curr - 2] + A[curr - 1] + A[curr]
        return 0


if __name__ == '__main__':
    solu = Solution()
    print solu.largestPerimeter([1,2,1])
