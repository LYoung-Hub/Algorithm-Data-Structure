from collections import defaultdict
import bisect


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hash_set = defaultdict(list)
        for i, w in enumerate(words):
            self.hash_set[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dis = float('Inf')
        for idx in self.hash_set[word2]:
            insert_idx = bisect.bisect(self.hash_set[word1], idx)
            if insert_idx == 0:
                min_dis = min(min_dis, abs(idx - self.hash_set[word1][0]))
            elif insert_idx == len(self.hash_set[word1]):
                min_dis = min(min_dis, abs(idx - self.hash_set[word1][-1]))
            else:
                min_dis = min(min_dis, min(abs(idx - self.hash_set[word1][insert_idx - 1]), abs(self.hash_set[word1][insert_idx]) - idx))
        return min_dis


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
