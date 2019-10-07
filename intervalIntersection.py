class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        length1 = len(A)
        length2 = len(B)
        idx1 = 0
        idx2 = 0
        ans = []
        while idx1 < length1 and idx2 < length2:
            low = max(A[idx1][0], B[idx2][0])
            high = min(A[idx1][1], B[idx2][1])

            if low <= high:
                ans.append([low, high])

            if A[idx1][1] < B[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.intervalIntersection([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]])
