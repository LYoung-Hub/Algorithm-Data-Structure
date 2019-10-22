class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = 0
        ans = []
        for a in A:
            if a % 2 == 0:
                s += a
        for q in queries:
            if A[q[1]] % 2 != 0 and q[0] % 2 != 0:
                s += A[q[1]] + q[0]
            elif A[q[1]] % 2 == 0 and q[0] % 2 != 0:
                s -= A[q[1]]
            elif A[q[1]] % 2 == 0 and q[0] % 2 == 0:
                s += q[0]
            A[q[1]] += q[0]
            ans.append(s)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]])
