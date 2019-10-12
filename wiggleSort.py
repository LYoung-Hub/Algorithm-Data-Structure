class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])
        nums[::2], nums[1::2] = nums[:mid], nums[mid:]


if __name__ == '__main__':
    solu = Solution()
    print solu.wiggleSort([1,5,1,1,6,4])
