class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        left = 1
        right = x // 2
        mid = left + (right - left) // 2

        while left < right:
            s = mid * mid
            l = (mid + 1) * (mid + 1)
            if s <= x < l:
                return mid
            elif x < s:
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) // 2

        return left
