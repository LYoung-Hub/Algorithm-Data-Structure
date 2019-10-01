class Solution(object):

    visited = {}
    should_delete = {}
    no_delete = False

    def BFS(self, board, i, j):
        row = len(board)
        col = len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col or (i, j) in self.visited:
            return

        if board[i][j] == 'X':
            self.visited[(i, j)] = True
            return

        if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == 'O':
            self.visited[(i, j)] = True
            self.should_delete = {}
            self.no_delete = True
            return

        if 0 < i < row - 1 and 0 < j < col - 1 and board[i][j] == 'O':
            self.visited[(i, j)] = True
            self.BFS(board, i + 1, j)
            self.BFS(board, i - 1, j)
            self.BFS(board, i, j + 1)
            self.BFS(board, i, j - 1)
            if not self.no_delete:
                self.should_delete[(i, j)] = [i, j]
                return

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.visited = {}
        self.should_delete = {}
        self.no_delete = False

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if (i, j) not in self.visited and board[i][j] == 'O':
                    self.BFS(board, i, j)
                    for v in self.should_delete.values():
                        board[v[0]][v[1]] = 'X'
                    self.should_delete = {}
                    self.no_delete = False


if __name__ == '__main__':
    solu = Solution()
    print solu.solve([["X","O","X","O","X","O","O","O","X","O"],["X","O","O","X","X","X","O","O","O","X"],["O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","X","O","O","X"],["O","O","X","X","O","X","X","O","O","O"],["X","O","O","X","X","X","O","X","X","O"],["X","O","X","O","O","X","X","O","X","O"],["X","X","O","X","X","O","X","O","O","X"],["O","O","O","O","X","O","X","O","X","O"],["X","X","O","X","X","X","X","O","O","O"]])
