import heapq as hq
from collections import deque


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    hq.heappush(heap, ((self.calValueOfPair(n1, n2)), [n1, n2]))
                elif self.calValueOfPair(n1, n2) > heap[0][0]:
                    hq.heapreplace(heap, ((self.calValueOfPair(n1, n2)), [n1, n2]))
        ans = deque([])
        while len(heap) > 0:
            ans.appendleft(hq.heappop(heap)[1])
        return ans

    def calValueOfPair(self, n1, n2):
        return -1 * (n1 + n2)


if __name__ == '__main__':
    solu = Solution()
    print solu.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3)
