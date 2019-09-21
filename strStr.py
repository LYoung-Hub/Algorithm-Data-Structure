class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if length == 0:
            return 0

        for i in range(0, len(haystack) - length + 1):
            idx = i
            needle_idx = 0
            while needle_idx < length and needle[needle_idx] == haystack[idx]:
                idx += 1
                needle_idx += 1
            if needle_idx == length:
                return i

        return -1


if __name__ == '__main__':
    solu = Solution()
    print solu.strStr('a', 'a')
