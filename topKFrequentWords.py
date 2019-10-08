from collections import Counter
import heapq as hq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = Counter(words)
        heap = [(-f, w) for w, f in cnt.items()]
        hq.heapify(heap)
        return [hq.heappop(heap)[1] for i in xrange(k)]


if __name__ == '__main__':
    solu = Solution()
    print solu.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
