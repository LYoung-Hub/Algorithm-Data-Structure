class Solution(object):

    ans = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        self.ans = []
        self.backTracking(nums, [])
        self.ans.append([])
        return self.ans

    def backTracking(self, nums, comb):
        for i in range(0, len(nums)):
            self.ans.append(comb + [nums[i]])
            self.backTracking(nums[:i], comb + [nums[i]])
