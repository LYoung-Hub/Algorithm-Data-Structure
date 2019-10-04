class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        shift = 31
        ans = 0
        while shift >= 0:
            ans += (n & 1) << shift
            n >>= 1
            shift -= 1
        return ans
