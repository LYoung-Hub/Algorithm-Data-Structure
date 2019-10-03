class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False

        length_s = len(s)
        length_t = len(t)

        if abs(length_t - length_s) > 1:
            return False

        if length_s == length_t:
            cnt = 0
            for i in range(0, length_t):
                if s[i] != t[i]:
                    cnt += 1
                if cnt > 1:
                    return False

        if length_s < length_t:
            i = 0
            while i < length_s and s[i] == t[i]:
                i += 1
            j = i + 1
            while i < length_s and s[i] == t[j]:
                i += 1
                j += 1
            if i != length_s:
                return False

        if length_s > length_t:
            i = 0
            while i < length_t and t[i] == s[i]:
                i += 1
            j = i + 1
            while i < length_t and t[i] == s[j]:
                i += 1
                j += 1
            if i != length_t:
                return False

        return True
