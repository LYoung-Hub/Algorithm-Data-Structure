from collections import deque


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        q = deque([1])
        ans = {1: 0}
        while q:
            curr = q.popleft()
            if curr == N * N:
                return ans[curr]
            for n in xrange(curr + 1, min(curr + 6, N * N) + 1):
                quotient, remainder = divmod(n - 1, N)
                r = N - 1 - quotient
                c = remainder if r % 2 != 0 else N - 1 - remainder
                if board[r][c] != -1:
                    n = board[r][c]
                if n not in ans:
                    ans[n] = ans[curr] + 1
                    q.append(n)
        return -1
