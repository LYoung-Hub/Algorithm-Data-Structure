class Solution(object):

    hash_set = {}

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])

        for i in range(0, row):
            for j in range(0, col):
                if word[0] == board[i][j]:
                    self.hash_set = {}
                    if self.DFS(board, word, 0, i, j):
                        return True

        return False

    def DFS(self, board, word, idx, i, j):
        row = len(board)
        col = len(board[0])

        if idx == len(word):
            return True

        if i < 0 or i >= row or j < 0 or j >= col or word[idx] != board[i][j]:
            return False

        if (i, j) in self.hash_set:
            return False
        else:
            self.hash_set[(i, j)] = 1

        flag = self.DFS(board, word, idx + 1, i - 1, j) or self.DFS(board, word, idx + 1, i + 1, j) \
            or self.DFS(board, word, idx + 1, i, j - 1) or self.DFS(board, word, idx + 1, i, j + 1)

        self.hash_set.pop((i, j))
        return flag


if __name__ == '__main__':
    solu = Solution()
    print solu.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
