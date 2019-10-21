class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        p = 0
        while num:
            curr = (num & 1) ^ 1
            ans += curr * 2 ** p
            p += 1
            num >>= 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.findComplement(5)
