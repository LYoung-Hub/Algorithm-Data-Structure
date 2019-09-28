class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tail_1 = m - 1
        tail_2 = n - 1
        curr = m + n - 1

        while tail_1 >= 0 and tail_2 >= 0:
            if nums2[tail_2] > nums1[tail_1]:
                nums1[curr] = nums2[tail_2]
                tail_2 -= 1
            else:
                nums1[curr] = nums1[tail_1]
                tail_1 -= 1
            curr -= 1

        nums1[:tail_2 + 1] = nums2[:tail_2 + 1]


if __name__ == '__main__':
    solu = Solution()
    solu.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)
