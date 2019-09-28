"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):

    visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        self.visited = {}
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.DFS(node)
        return node_copy

    def DFS(self, node):
        for n in node.neighbors:
            if n not in self.visited:
                node_copy = Node(n.val, [])
                self.visited[n] = node_copy
                self.visited[node].neighbors.append(node_copy)
                self.DFS(n)
            else:
                self.visited[node].neighbors.append(self.visited[n])


