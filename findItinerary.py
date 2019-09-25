class Solution(object):

    def compareLexica(self, s, t):
        for i in range(0, 3):
            if ord(s[i]) > ord(t[i]):
                return False
            elif ord(s[i]) < ord(t[i]):
                return True

        return True

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        length = len(tickets)
        if length == 0:
            return []

        hash_set = {}
        for t in tickets:
            if t[0] not in hash_set:
                hash_set[t[0]] = [t[1]]
            else:
                curr = len(hash_set[t[0]]) - 1
                if not self.compareLexica(t[1], hash_set[t[0]][0]):
                    hash_set[t[0]].insert(0, t[1])
                else:
                    while curr >= 0:
                        if self.compareLexica(t[1], hash_set[t[0]][curr]):
                            hash_set[t[0]].insert(curr + 1, t[1])
                            break
                        else:
                            curr -= 1

        ans = []

        def DFS(graph, node):
            ans.append(node)
            if len(ans) == length + 1:
                return True

            if node in graph:
                n, i = len(graph[node]), 0
                while i < n:
                    A = graph[node].pop()
                    if DFS(graph, A):
                        return True
                    graph[node] = [A] + graph[node]
                    i += 1
            ans.pop()
            return False

        DFS(hash_set, 'JFK')

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],
                              ["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],
                              ["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],
                              ["EZE","ANU"],["AUA","ANU"]])
