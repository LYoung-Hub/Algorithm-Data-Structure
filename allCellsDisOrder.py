import heapq as hq


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        heap = []
        for x in xrange(R):
            for y in xrange(C):
                d = abs(x - r0) + abs(y - c0)
                hq.heappush(heap, [d, [x, y]])
        ans = []
        while heap:
            ans.append(hq.heappop(heap)[1])
        return ans
