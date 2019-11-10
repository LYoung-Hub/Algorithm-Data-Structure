class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right = bound = len(nums) - 1
        while right >= 0:
            while right >= 0 and nums[right] != 0:
                right -= 1
            if right >= 0 and nums[right] == 0:
                curr = right
                while curr < bound:
                    nums[curr], nums[curr + 1] = nums[curr + 1], nums[curr]
                    curr += 1
                bound -= 1
            right -= 1


if __name__ == '__main__':
    solu = Solution()
    print solu.moveZeroes([1, 0])
