class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1

        if length == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        left = 0
        right = length - 1
        mid = left + (right - left) / 2

        while left <= right:
            if nums[mid] == target:
                return mid

            if left == right:
                return -1

            if nums[mid] <= nums[mid + 1]:
                if nums[left] > nums[mid]:
                    if target >= nums[left] or target < nums[mid]:
                        right = mid
                    elif nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        return -1
                else:
                    if nums[left] <= target < nums[mid]:
                        right = mid
                    elif target <= nums[right] or target > nums[mid]:
                        left = mid + 1
                    else:
                        return -1
            else:
                if target >= nums[left]:
                    right = mid
                elif target <= nums[right]:
                    left = mid + 1
                else:
                    return -1

            mid = left + (right - left) / 2

        return -1


if __name__ == '__main__':
    solu = Solution()
    print solu.search([1, 3], 0)
