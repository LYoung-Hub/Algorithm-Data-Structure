from collections import deque


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        nums = deque()
        while x > 0:
            num = x % 10
            nums.append(num)
            x = x / 10

        while len(nums) > 1:
            if nums.pop() != nums.popleft():
                return False

        return True


if __name__ == '__main__':
    solu = Solution()
    print solu.isPalindrome(-121)


