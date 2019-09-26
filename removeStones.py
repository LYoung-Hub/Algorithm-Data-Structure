class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        union = unionFind(20000)
        for x, y in stones:
            union.join(x, y + 10000)

        return N - len({union.find(x) for x, y in stones})


class unionFind(object):

    parent = []

    def __init__(self, N):
        self.parent = range(N)

    def find(self, x):
        while self.parent[x] != x:
                x = self.parent[x]
        return x

    def join(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        self.parent[fx] = fy
