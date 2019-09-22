class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        length = len(nums)
        if lower == upper:
            if length == 0:
                return [str(lower)]
            else:
                return []

        if length == 0:
            return [str(lower) + '->' + str(upper)]

        ans = []

        if lower < nums[0] - 1:
            ans.append(str(lower) + '->' + str(nums[0] - 1))
        elif lower == nums[0] - 1:
            ans.append(str(lower))

        for i in range(0, length - 1):
            if nums[i + 1] - nums[i] == 2:
                ans.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                ans.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))

        if upper > nums[-1] + 1:
            ans.append(str(nums[-1] + 1) + '->' + str(upper))
        elif upper == nums[-1] + 1:
            ans.append(str(upper))

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.findMissingRanges([1, 3], 0, 9)
