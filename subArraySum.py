from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        hash_set = defaultdict(int)
        hash_set[0] = 1
        ans = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in hash_set:
                ans += hash_set[curr_sum - k]
            hash_set[curr_sum] += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.subarraySum([1,1,1], 2)
