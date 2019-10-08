import heapq as hq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            if len(heap) < k:
                hq.heappush(heap, n)
            else:
                if n > heap[0]:
                    hq.heappop(heap)
                    hq.heappush(heap, n)
        return heap[0]
