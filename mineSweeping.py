import random


class Solution(object):
    def generateMines(self, row, col, mines):
        hash_set = {}
        result = [[0 for _ in xrange(col)] for _ in xrange(row)]
        ran = row * col
        while mines > 0:
            chosen = int(random.random() * ran)
            ran -= 1
            final_chosen = hash_set.get(chosen, chosen)
            hash_set.setdefault(chosen, hash_set.get(ran, ran))
            result[final_chosen // col][final_chosen % col] = 1
            mines -= 1
        return result


if __name__ == '__main__':
    solu = Solution()
    print solu.generateMines(3, 2, 3)
