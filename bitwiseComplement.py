class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        power = 0
        while N:
            curr = (N & 1) ^ 1
            N >>= 1
            ans += curr * 2 ** power
            power += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.bitwiseComplement(5)
