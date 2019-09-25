from collections import defaultdict
import heapq as hq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        visited = {}
        dis = [(0, K)]
        while dis:
            d, curr = hq.heappop(dis)
            if curr in visited:
                continue
            next_nodes = graph[curr]
            for ne in next_nodes:
                if ne[0] not in visited:
                    hq.heappush(dis, (d + ne[1], ne[0]))
            visited[curr] = d

        return max(visited.values()) if len(visited) == N else -1


if __name__ == '__main__':
    solu = Solution()
    print solu.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1)
