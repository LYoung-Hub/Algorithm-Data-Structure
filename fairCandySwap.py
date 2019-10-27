from collections import defaultdict


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        set_b = defaultdict(int)
        for b in B:
            set_b[b] = 0
        diff = sum(A) - sum(B)
        for a in A:
            if a - diff / 2 in set_b:
                return [a, a - diff / 2]


if __name__ == '__main__':
    solu = Solution()
    print solu.fairCandySwap([2],[1,3])
