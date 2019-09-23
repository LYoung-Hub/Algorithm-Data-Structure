class Solution(object):

    ans = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        length = len(nums)
        if length == 0:
            return []

        nums.sort()
        self.ans.append(nums)

        cnt = self.permutationCount(length)
        duplication = [1]
        for i in range(1, length):
            if nums[i - 1] == nums[i]:
                duplication[-1] += 1
            else:
                duplication.append(1)

        for i in range(0, len(duplication)):
            cnt /= self.permutationCount(duplication[i])

        for i in range(1, cnt):
            self.nextPermutation(self.ans[-1])

        return self.ans

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        next_nums = nums[:]
        if length > 0:
            tail = length - 1
            curr = tail
            while curr > 0 and next_nums[curr] <= next_nums[curr - 1]:
                curr -= 1

            if curr == 0:
                self.reverse(next_nums, 0, length - 1)
            else:
                change_point = curr
                while change_point < length and next_nums[curr - 1] < next_nums[change_point]:
                    change_point += 1
                next_nums[change_point - 1], next_nums[curr - 1] = next_nums[curr - 1], next_nums[change_point - 1]
                if curr < length:
                    self.reverse(next_nums, curr, length - 1)
        self.ans.append(next_nums)

    def reverse(self, nums, start, stop):
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

    def permutationCount(self, n):
        ans = 1
        for i in range(0, n):
            ans = ans * (i + 1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.permute([2, 2, 3, 3, 3])
