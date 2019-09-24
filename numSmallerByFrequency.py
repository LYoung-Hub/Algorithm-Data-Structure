class Solution(object):

    def f(self, s):
        min_ascii = 257
        for e in s:
            ascii = ord(e)
            if ascii < min_ascii:
                min_ascii = ascii
        return s.count(chr(min_ascii))

    def binarySearch(self, target, nums):
        length = len(nums)

        if target < nums[0]:
            return length
        if target > nums[-1]:
            return 0

        left = 0
        right = length - 1
        mid = left + (right - left) / 2
        while left < right:
            if nums[mid] <= target < nums[mid + 1]:
                return length - mid - 1
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) / 2
        return length - left - 1

    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        f_queries = []
        for q in queries:
            f_queries.append(self.f(q))

        f_words = []
        for w in words:
            f_words.append(self.f(w))
        f_words.sort()

        ans = []
        for f in f_queries:
            ans.append(self.binarySearch(f, f_words))

        return ans
