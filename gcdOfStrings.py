class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len_one, len_two = len(str1), len(str2)
        if len_one < len_two:
            return self.gcdOfStrings(str2, str1)

        if str1[:len_two] == str2:
            if len_one == len_two:
                return str2
            return self.gcdOfStrings(str1[len_two:], str2)
        return ''


if __name__ == '__main__':
    solu = Solution()
    print solu.gcdOfStrings("ABABAB", "ABAB")
