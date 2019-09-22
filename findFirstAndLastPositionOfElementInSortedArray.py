class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)

        if length == 0:
            return [-1, -1]

        if length == 1 and nums[0] == target:
            return [0, 0]

        left = 0
        right = length - 1
        mid = left + (right - left) / 2

        ans = [-1, -1]
        while left <= right:
            if nums[mid] == target:
                first = mid
                while first > 0 and nums[first] == nums[first - 1]:
                    first -= 1
                ans[0] = first
                last = mid
                while last < length - 1 and nums[last] == nums[last + 1]:
                    last += 1
                ans[1] = last
                return ans
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = left + (right - left) / 2

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.searchRange([5, 7, 7, 8, 8, 10], 5)
