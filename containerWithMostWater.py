class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if area > max_area:
                max_area = area

        return max_area
