class Solution(object):

    ans = []

    def subarrayProduct(self, nums):
        if len(nums) == 0:
            return []
        self.ans = []
        self.backtracking(nums, [])
        print self.ans

    def backtracking(self, nums, comb):
        if len(nums) == 0:
            return

        for i in range(0, len(nums)):
            self.ans.append(comb + [nums[i]])
            self.backtracking(nums[i + 1:], comb + [nums[i]])


if __name__ == '__main__':
    solu = Solution()
    print solu.subarrayProduct([2, 7, 11])
