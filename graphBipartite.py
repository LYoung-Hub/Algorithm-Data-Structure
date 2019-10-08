class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        for node in xrange(len(graph)):
            if node not in color:
                color[node] = 0
                stack = [node]
                while stack:
                    n = stack.pop()
                    for chd in graph[n]:
                        if chd not in color:
                            color[chd] = color[n] ^ 1
                            stack.append(chd)
                        elif color[chd] == color[n]:
                            return False
        return True
