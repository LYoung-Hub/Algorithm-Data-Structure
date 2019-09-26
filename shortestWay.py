class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        ans = 0
        length_s = len(source)
        length_t = len(target)

        s = 0
        t = 0
        while t < length_t:
            if source.find(target[t]) == -1:
                return -1
            while s < length_s and t < length_t:
                if source[s] == target[t]:
                    s += 1
                    t += 1
                else:
                    s += 1
            ans += 1
            s = 0

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.shortestWay("bxdisnclwdrpcqamhqqvudgtdbsdikhzzbnlgzlspozvhdkunxkpevnqvyrfowanagolpwvezuvnhgxvjopcvrkdaippmwgkofbo", "ntzebqmlrzxissncdlvcxbojgbnnphtfdunjpzroegfdvieaajafjkidpxbrgsjpgmalekhjckwgygfz")
