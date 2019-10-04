class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        cnt = 0
        start = 0
        while cnt < length:
            curr = start
            pre = nums[curr]
            next_idx = (curr + k) % length
            temp = nums[next_idx]
            nums[next_idx] = pre
            pre = temp
            curr = next_idx
            cnt += 1
            while start != curr:
                next_idx = (curr + k) % length
                temp = nums[next_idx]
                nums[next_idx] = pre
                pre = temp
                curr = next_idx
                cnt += 1
            start += 1
