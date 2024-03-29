# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = left + (right - left) / 2
        while left < right:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) / 2
        return left
