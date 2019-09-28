class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        leftmost_two = length - 1
        rightmost_zero = 0
        curr = 0

        while curr <= leftmost_two:
            if nums[curr] == 0:
                nums[curr], nums[rightmost_zero] = nums[rightmost_zero], nums[curr]
                rightmost_zero += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[leftmost_two] = nums[leftmost_two], nums[curr]
                leftmost_two -= 1
            else:
                curr += 1


if __name__ == '__main__':
    solu = Solution()
    solu.sortColors([2,0,1])
