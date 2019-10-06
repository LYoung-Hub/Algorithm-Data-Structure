class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target, length = sum(nums), len(nums)
        if target == 0 or target % 2 != 0:
            return False

        target = target / 2
        dp = [True] + [False] * target
        for n in nums:
            dp = [(dp[s] or (s >= n and dp[s - n])) for s in range(target + 1)]
            if dp[target]:
                return True
        return False


if __name__ == '__main__':
    solu = Solution()
    print solu.canPartition([1,2,3,5])
