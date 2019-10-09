class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def nextDays(cells):
            return [int(0 < i < 7 and cells[i - 1] == cells[i + 1]) for i in range(0, 8)]

        visited = {}
        while N > 0:
            c = tuple(cells)
            if c in visited:
                N %= visited[c] - N
            visited[c] = N

            if N > 0:
                N -= 1
                cells = nextDays(cells)
        return cells
