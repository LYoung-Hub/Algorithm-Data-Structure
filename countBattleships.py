class Solution(object):
    R = 0
    C = 0

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        self.R = len(board)
        self.C = len(board[0])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    self.DFS(r, c, board)
                    ans += 1
        return ans

    def DFS(self, row, col, board):
        if row < 0 or row > self.R - 1 or col < 0 or col > self.C - 1 or board[row][col] != 'X':
            return
        board[row][col] = '1'
        self.DFS(row + 1, col, board)
        self.DFS(row - 1, col, board)
        self.DFS(row, col + 1, board)
        self.DFS(row, col - 1, board)


if __name__ == '__main__':
    solu = Solution()
    print solu.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
