import heapq as hq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        length = len(intervals)
        if length == 0:
            return 0

        def takeFirst(tup):
            return tup[0]

        intervals.sort(key=takeFirst)

        heap = []
        hq.heappush(heap, intervals[0][1])

        for i in range(1, length):
            if intervals[i][0] < heap[0]:
                hq.heappush(heap, intervals[i][1])
            else:
                hq.heapreplace(heap, intervals[i][1])

        return len(heap)


if __name__ == '__main__':
    solu = Solution()
    print solu.minMeetingRooms([[7,10],[2,4]])
