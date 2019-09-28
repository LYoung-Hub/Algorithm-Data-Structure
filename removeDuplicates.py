class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return length

        left = 0
        right = 1
        count = 1
        while right < length:
            if nums[right] != nums[right - 1]:
                nums[left + 1] = nums[right]
                left += 1
                count = 1
            elif count == 1:
                nums[left + 1] = nums[right]
                left += 1
                count += 1
            right += 1

        return left + 1


if __name__ == '__main__':
    solu = Solution()
    print solu.removeDuplicates([1,1,1,2,2,3])
