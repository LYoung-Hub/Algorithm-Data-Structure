class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        dp = [1]
        for i in range(1, length):
            temp = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    temp = max(dp[j], temp)
            dp.append(temp + 1)

        return max(dp)
