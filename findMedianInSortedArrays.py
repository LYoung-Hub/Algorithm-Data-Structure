class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        iMin = 0
        iMax = m
        while iMin <= iMax:
            i = (iMin + iMax) / 2
            j = (m + n + 1) / 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                iMax = i - 1
            elif i < m and nums1[i] < nums2[j - 1]:
                iMin = i + 1
            else:
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 != 0:
                    return left_max

                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2.0


if __name__ == '__main__':
    solu = Solution()
    print solu.findMedianSortedArrays([4, 5], [1, 2, 3])
