class Solution(object):
    class UnionFind(object):

        def __init__(self, n):
            self.parent = [0]
            for i in xrange(n):
                self.parent.append(i + 1)

        def find(self, x):
            while x != self.parent[x]:
                x = self.find(self.parent[x])
            return x

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px == py:
                return False
            else:
                self.parent[py] = px
                return True

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        un = self.UnionFind(len(edges))
        for edge in edges:
            if not un.union(edge[0], edge[1]):
                return edge


if __name__ == '__main__':
    solu = Solution()
    print solu.findRedundantConnection([[1,2],[1,3],[2,3]])
