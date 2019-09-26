class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n + 1)]

        for i in range(0, k - 1):
            self.nextPermutation(nums)

        ans = ''
        for n in nums:
            ans += str(n)

        return ans

    def nextPermutation(self, nums):
        length = len(nums)
        if length > 0:
            tail = length - 1
            curr = tail
            while curr > 0 and nums[curr] <= nums[curr - 1]:
                curr -= 1

            if curr == 0:
                self.reverse(nums, 0, length - 1)
            else:
                change_point = curr
                while change_point < length and nums[curr - 1] < nums[change_point]:
                    change_point += 1
                nums[change_point - 1], nums[curr - 1] = nums[curr - 1], nums[change_point - 1]
                if curr < length:
                    self.reverse(nums, curr, length - 1)

    def reverse(self, nums, start, stop):
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1


if __name__ == '__main__':
    solu = Solution()
    print solu.getPermutation(3, 3)
