import heapq as hq
import math


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for i, p in enumerate(points):
            dis = -1 * self.calDis(p)
            if len(heap) < K:
                hq.heappush(heap, (dis, i))
            else:
                if dis > heap[0][0]:
                    hq.heappop(heap)
                    hq.heappush(heap, (dis, i))

        ans = []
        for h in heap:
            ans.append(points[h[1]])
        return ans

    def calDis(self, point):
        return math.sqrt(point[0] * point[0] + point[1] * point[1])


if __name__ == '__main__':
    solu = Solution()
    print solu.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3)
