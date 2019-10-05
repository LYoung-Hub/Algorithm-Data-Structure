class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        idx1, idx2 = 0, 0
        length1, length2 = len(nums1), len(nums2)

        ans = []
        while idx1 < length1 and idx2 < length2:
            if nums1[idx1] == nums2[idx2]:
                ans.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
                continue
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.intersect([4,9,5], [9,4,9,8,4])
