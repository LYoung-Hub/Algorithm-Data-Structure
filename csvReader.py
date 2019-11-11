import csv
import heapq as hq


class Solution(object):
    def rank(self, f, n):
        f_id = open(f, 'r')
        reader = csv.reader(f_id)
        res = {}
        for item in reader:
            if reader.line_num == 1:
                continue
            res[item[0]] = item[1]
        heap = []
        for k, v in res.items():
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
    solu.rank('test.csv', 2)
