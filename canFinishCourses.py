from collections import deque, defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        todo = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)
        for k, v in prerequisites:
            todo[k].add(v)
            graph[v].add(k)

        q = deque([])
        for k, v in todo.items():
            if len(todo[k]) == 0:
                q.append(k)

        while q:
            node = q.popleft()
            for c in graph[node]:
                todo[c].remove(node)
                if len(todo[c]) == 0:
                    q.append(c)
            todo.pop(node)

        return len(todo) == 0
