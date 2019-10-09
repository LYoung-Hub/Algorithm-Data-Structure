from collections import deque


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        row = len(maze)
        if row == 0:
            return -1
        col = len(maze[0])
        if col == 0:
            return -1

        dis = [[float('Inf') for i in xrange(col)] for j in xrange(row)]
        dis[start[0]][start[1]] = 0
        q = deque([start])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            curr = q.popleft()
            for d in direction:
                x = curr[0] + d[0]
                y = curr[1] + d[1]
                cnt = 0
                while 0 <= x < row and 0 <= y < col and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                    cnt += 1
                if dis[curr[0]][curr[1]] + cnt < dis[x - d[0]][y - d[1]]:
                    dis[x - d[0]][y - d[1]] = dis[curr[0]][curr[1]] + cnt
                    q.append([x - d[0], y - d[1]])
        return dis[destination[0]][destination[1]] if dis[destination[0]][destination[1]] < float('Inf') else -1


if __name__ == '__main__':
    solu = Solution()
    print solu.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4])
