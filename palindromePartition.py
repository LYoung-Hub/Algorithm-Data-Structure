class Solution(object):

    ans = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []

        self.ans = []
        self.backTracking(s, [])
        return self.ans

    def isPalindrome(self, s):
        length = len(s)
        left = 0
        right = length - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backTracking(self, s, comb):
        length = len(s)
        if length == 0:
            self.ans.append(comb)
            return

        for i in range(1, length + 1):
            if self.isPalindrome(s[:i]):
                self.backTracking(s[i:], comb + [s[:i]])
