class Solution(object):

    def takeFirst(self, interval):
        return interval[0]

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(intervals)
        ans = []
        if length == 0:
            return ans

        intervals.sort(key=self.takeFirst)

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.merge([[1,3],[2,6],[8,10],[15,18]])
