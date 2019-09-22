class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hash_set = {}
        for ns, nt in zip(s, t):
            if ns not in hash_set:
                if nt in hash_set.values():
                    return False
                hash_set[ns] = nt
            else:
                if hash_set[ns] != nt:
                    return False

        return True
