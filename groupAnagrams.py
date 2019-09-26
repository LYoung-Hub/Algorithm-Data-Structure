from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_set = defaultdict(list)

        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            hash_set[tuple(alpha)].append(s)

        return hash_set.values()
