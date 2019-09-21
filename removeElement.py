class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        left = 0
        right = length - 1

        while left < right:
            if nums[left] == val:
                while left < right and nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            else:
                left += 1

        if nums[left] == val:
            return left
        else:
            return left + 1


if __name__ == '__main__':
    solu = Solution()
    print solu.removeElement([1, 1, 1, 1], 1)
