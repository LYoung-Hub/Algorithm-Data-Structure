class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return []

        nums.sort()

        ans = []
        min_err = 10000
        for i in range(0, length - 2):
            left = i + 1
            right = length - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                err = three_sum - target

                if err < 0:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif err > 0:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    ans = three_sum
                    return ans

                if abs(err) < min_err:
                    ans = three_sum
                    min_err = abs(err)

        return ans
