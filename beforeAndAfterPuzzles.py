from collections import defaultdict


class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        first = defaultdict(list)
        last = defaultdict(list)
        for i, p in enumerate(phrases):
            strs = p.split()
            first[strs[0]].append(i)
        ans = defaultdict(int)
        for i, p in enumerate(phrases):
            strs = p.split()
            if strs[-1] in first:
                for k in first[strs[-1]]:
                    if k != i:
                        if len(strs) > 1:
                            tmp = ' '.join(strs[:-1]) + ' ' + phrases[k]
                        else:
                            tmp = phrases[k]
                        ans[tmp] = 1
        return sorted(ans.keys())


if __name__ == '__main__':
    solu = Solution()
    print solu.beforeAndAfterPuzzles(["writing code","code rocks"])
