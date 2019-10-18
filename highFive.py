from collections import defaultdict
import heapq as hq


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        for i in items:
            d[i[0]].append(i[1])
        heap = []
        for k, v in d.items():
            d[k].sort()
            hq.heappush(heap, [k, sum(d[k][-5:]) / 5])
        ans = []
        while heap:
            ans.append(hq.heappop(heap))
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
