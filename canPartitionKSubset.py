class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, remainder = divmod(sum(nums), k)
        if remainder:
            return False

        def search(groups):
            if not nums:
                return True
            v = nums.pop()
            for i, g in enumerate(groups):
                if g + v <= target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not g:
                    break
            nums.append(v)
            return False

        nums = sorted(nums)
        if nums[-1] > target: return False
        while nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
