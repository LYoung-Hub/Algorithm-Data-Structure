class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0 or target <= nums[0]:
            return 0

        if target > nums[length - 1]:
            return length

        left = 0
        right = length - 1
        mid = left + (right - left) / 2

        while left <= right:
            if mid > 0 and nums[mid - 1] < target < nums[mid]:
                return mid

            if target == nums[mid]:
                pos = mid
                while pos > 0 and nums[pos] == nums[pos - 1]:
                    pos -= 1
                return pos
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = left + (right - left) / 2
