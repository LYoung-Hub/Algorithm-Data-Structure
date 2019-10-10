class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    i = r + n[0]
                    j = c + n[1]
                    if 0 <= i < rows and 0 <= j < cols and abs(board[i][j]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] > 0 else 0


if __name__ == '__main__':
    solu = Solution()
    print solu.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
