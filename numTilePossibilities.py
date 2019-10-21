from collections import defaultdict


class Solution(object):
    hash_set = defaultdict()

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.hash_set = defaultdict()
        for i in range(1, len(tiles) + 1):
            self.backTracking(tiles, '', i)
        return len(self.hash_set)

    def backTracking(self, nums, comb, k):
        if len(comb) == k:
            self.hash_set[comb] = 1
            return

        for i in range(0, len(nums)):
            self.backTracking(nums[:i] + nums[i + 1:], comb + nums[i], k)


if __name__ == '__main__':
    solu = Solution()
    print solu.numTilePossibilities('AAB')
