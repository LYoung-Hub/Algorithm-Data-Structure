class Solution(object):

    key_board = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    combinations = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        self.combinations = []

        self.backTracking('', digits)

        return self.combinations

    def backTracking(self, combination, digits):
        if len(digits) == 1:
            for i in range(0, len(self.key_board[digits[0]])):
                self.combinations.append(combination + self.key_board[digits[0]][i])
            return

        curr = digits[0]
        for i in range(0, len(self.key_board[curr])):
            self.backTracking(combination + self.key_board[curr][i], digits[1:])


if __name__ == '__main__':
    solu = Solution()
    print solu.letterCombinations('22')
