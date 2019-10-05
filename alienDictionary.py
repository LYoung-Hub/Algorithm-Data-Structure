class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(0, len(words) - 1):
            diff = False
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    diff = True
                    if order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False
                    break
            if not diff:
                if len(words[i]) > len(words[i + 1]):
                    return False
        return True


if __name__ == '__main__':
    solu = Solution()
    print solu.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
