class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_set = {0: -1}
        s = 0
        for i in range(0, len(nums)):
            s += nums[i]
            if k != 0:
                s = s % k
            if s not in hash_set:
                hash_set[s] = i
            else:
                if i - hash_set[s] > 1:
                    return True

        return False
