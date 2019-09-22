class Solution(object):

    ans = []

    def combinationSum2(self, candidates, target):
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
        candidates.sort()
        self.backTracking(candidates, target, comb)

        return self.ans

    def backTracking(self, nums, target, comb):
        if target == 0:
            self.ans.append(comb)
            return

        if target < 0:
            return

        if len(nums) == 1:
            self.backTracking([], target - nums[0], comb + [nums[0]])
        else:
            for i in range(0, len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                self.backTracking(nums[i + 1:], target - nums[i], comb + [nums[i]])


if __name__ == '__main__':
    solu = Solution()
    print solu.combinationSum2([10,1,2,7,6,1,5], 8)
