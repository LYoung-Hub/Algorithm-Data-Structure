class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        f = 1
        for i in range(1, n):
            f = f * i

        N = n - 1
        nums = [i for i in range(1, n + 1)]
        k -= 1

        ans = []
        while N > 0:
            idx = k // f
            ans.append(nums[idx])
            nums.remove(nums[idx])
            k = k % f
            f = f / N
            N -= 1

        ans.append(nums[0])

        aim = ''
        for i in range(0, len(ans)):
            aim += str(ans[i])

        return aim


if __name__ == '__main__':
    solu = Solution()
    print solu.getPermutation(3, 3)
