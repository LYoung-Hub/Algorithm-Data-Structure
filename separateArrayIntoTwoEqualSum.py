class Solution(object):
    def separateArrayIntoTwoEqualSum(self, nums):
        split_point = 1
        left_sum = nums[0]
        right_sum = sum(nums[1:])
        while split_point < len(nums):
            if left_sum == right_sum:
                return split_point
            elif left_sum < right_sum:
                left_sum += nums[split_point]
                right_sum -= nums[split_point]
                split_point += 1
            else:
                return -1
        return split_point


if __name__ == '__main__':
    solu = Solution()
    print solu.separateArrayIntoTwoEqualSum([1, 5, 2, 3])
    print solu.separateArrayIntoTwoEqualSum([1, 2, 3, 4, 5, 5])
