from collections import Counter
import heapq as hq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
        heap = []
        for v, c in cnt.items():
            if len(heap) < k:
                hq.heappush(heap, (c, v))
            else:
                if c > heap[0][0]:
                    hq.heapreplace(heap, (c, v))
        return [h[1] for h in heap]


if __name__ == '__main__':
    solu = Solution()
    print solu.topKFrequent([4,1,-1,2,-1,2,3], 2)
