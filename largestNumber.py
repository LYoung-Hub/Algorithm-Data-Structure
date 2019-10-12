class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_str = ''.join(sorted(map(str, nums), cmp=lambda x, y: cmp(x + y, y + x), reverse=True))
        return '0' if largest_str[0] == '0' else largest_str

