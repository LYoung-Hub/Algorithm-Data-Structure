from collections import defaultdict


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length == 0:
            return 0

        hash_set = defaultdict(list)
        for x, y in points:
            hash_set[x].append(y)

        min_area = float('Inf')
        last_x = {}
        for col_key in sorted(hash_set):
            col = hash_set[col_key]
            col.sort()
            for i, y2 in enumerate(col):
                for j in range(0, i):
                    y1 = col[j]
                    if (y1, y2) in last_x:
                        area = (y2 - y1) * (col_key - last_x[(y1, y2)][-1])
                        if area < min_area:
                            min_area = area
                        last_x[(y1, y2)].append(col_key)
                    else:
                        last_x[(y1, y2)] = [col_key]

        return min_area if min_area < float('Inf') else 0


if __name__ == '__main__':
    solu = Solution()
    print solu.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])
