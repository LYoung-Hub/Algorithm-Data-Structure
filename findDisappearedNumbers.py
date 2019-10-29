class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        curr = 0
        while curr < len(nums):
            while nums[curr] != curr + 1 and nums[curr] != nums[nums[curr] - 1]:
                temp = nums[curr]
                nums[curr] = nums[nums[curr] - 1]
                nums[temp - 1] = temp
            curr += 1
        for i, n in enumerate(nums):
            if n != i + 1:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.findDisappearedNumbers([4,3,2,7,8,2,3,1])
