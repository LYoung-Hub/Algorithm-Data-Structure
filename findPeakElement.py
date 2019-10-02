class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, left, right):
        if left == right:
            return 1

        mid = left + (right - left) / 2
        if nums[mid] > nums[mid + 1]:
            return self.binarySearch(nums, left, mid - 1)
        return self.binarySearch(nums, mid, right)
