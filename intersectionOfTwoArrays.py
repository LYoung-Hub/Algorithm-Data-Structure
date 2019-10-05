from collections import defaultdict


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_set1 = defaultdict(int)
        hash_set2 = defaultdict(int)

        for n in nums1:
            hash_set1[n] = 1

        for n in nums2:
            hash_set2[n] = 1

        ans = []
        for k in hash_set1:
            if k in hash_set2:
                ans.append(k)

        return ans
