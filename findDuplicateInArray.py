class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        for i in xrange(n):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            i += 1
