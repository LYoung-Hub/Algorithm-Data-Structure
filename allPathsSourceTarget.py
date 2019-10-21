from collections import defaultdict


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        g = defaultdict(list)
        for i in xrange(len(graph)):
            g[i] = graph[i]
        stack = [0]
        visited = {}
        ans = []
        path = []
        while stack:
            node = stack.pop()
            if node not in visited:
                path.append(node)
                visited[node] = 1
                stack.extend(g[node])
                if node == len(graph) - 1:
                    ans.append(path)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.allPathsSourceTarget([[1,2],[3],[3],[]])
