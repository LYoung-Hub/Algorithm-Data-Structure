class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = len(A[0])
        ans = 0
        for i in xrange(n):
            temp = ''.join([a[i] for a in A])
            if temp != ''.join(sorted(temp)):
                ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.minDeletionSize(["cba","daf","ghi"])
