class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)
        i = 0
        while i < len(nums):
            while nums[i] != i and nums[i] != -1:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            i += 1
        for i, n in enumerate(nums):
            if n == -1:
                return i


if __name__ == '__main__':
    solu = Solution()
    print solu.missingNumber([3, 0, 1])
