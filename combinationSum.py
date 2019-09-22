class Solution(object):

    ans = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(candidates)
        if length == 0:
            return []

        self.ans = []
        comb = []
        self.backTracking(candidates, target, comb)

        return self.ans

    def backTracking(self, nums, target, comb):
        if target == 0:
            self.ans.append(comb)
            return

        if target < 0:
            return

        for i in range(0, len(nums)):
            self.backTracking(nums[i:], target - nums[i], comb + [nums[i]])


if __name__ == '__main__':
    solu = Solution()
    print solu.combinationSum([2, 3, 6, 7], 7)
