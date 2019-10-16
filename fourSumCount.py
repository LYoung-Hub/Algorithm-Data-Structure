class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        hash_set = {}
        for n1 in A:
            for n2 in B:
                temp = n1 + n2
                if temp not in hash_set:
                    hash_set[temp] = 1
                else:
                    hash_set[temp] += 1
        for n3 in C:
            for n4 in D:
                temp = 0 - (n3 + n4)
                if temp in hash_set:
                    ans += hash_set[temp]

        return ans
