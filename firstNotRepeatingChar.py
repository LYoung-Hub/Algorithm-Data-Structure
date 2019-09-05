# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        hash_set = {}
        for i in range(0, len(s)):
            if s[i] not in hash_set:
                hash_set[s[i]] = 1
                if s.count(s[i]) == 1:
                    return i

        return -1


if __name__ == '__main__':
    solu = Solution()
    solu.FirstNotRepeatingChar('google')
