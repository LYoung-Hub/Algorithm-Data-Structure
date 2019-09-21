class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        j = 0
        for i in range(1, length):
            if nums[i] > nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == '__main__':
    solu = Solution()
    print solu.removeDuplicates([0,0,0,0,0,1,2,2,3,3,4,4])
