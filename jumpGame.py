class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        dp = [nums[0]]
        for i in range(1, length):
            if i <= dp[-1]:
                dp.append(max(i + nums[i], dp[-1]))
            else:
                return False

            if dp[-1] >= length - 1:
                return True

        return True
