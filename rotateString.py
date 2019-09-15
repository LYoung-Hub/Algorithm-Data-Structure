class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if len(s) == 0:
            return ""

        if offset == 0:
            return s

        if offset > len(s):
            offset = offset % len(s)

        temp = ""
        tail = len(s) - 1
        for i in range(0, offset):
            temp = s[tail] + temp
            tail -= 1

        result = str(temp) + str(s[0:len(s) - offset])
        return result


if __name__ == '__main__':
    solu = Solution()
    print solu.rotateString("abcdefg", 3)
