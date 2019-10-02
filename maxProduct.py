class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, curr_min, ans = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            tmp = curr_max
            curr_max = max(n, n * curr_max, n * curr_min)
            curr_min = min(n, n * curr_min, n * tmp)
            ans = max(ans, curr_max)
        return ans
