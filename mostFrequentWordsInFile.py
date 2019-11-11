import heapq as hq
from collections import Counter


class Solution(object):
    def printMostFrequentWordsInFile(self, f, n):
        f_id = open(f)
        content = f_id.readlines()
        for i in xrange(len(content)):
            content[i] = content[i].strip('\n')
        cnt = Counter(content)
        heap = []
        for k, v in cnt.items():
            if len(heap) < n:
                hq.heappush(heap, (v, k))
            else:
                if v > heap[0][0]:
                    hq.heappop(heap)
                    hq.heappush(heap, (v, k))
        while heap:
            tmp = hq.heappop(heap)
            print tmp[1]
        f_id.close()
        return


if __name__ == '__main__':
    solu = Solution()
    print solu.printMostFrequentWordsInFile('test.txt', 2)
