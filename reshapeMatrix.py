class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums

        arr = []
        for i in xrange(row):
            arr.extend(nums[i])
        ans = []
        for j in xrange(r):
            ans.append(arr[j * c: j * c + c])
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.matrixReshape([[1,2],[3,4]],4, 1)
