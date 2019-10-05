class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or self.isPalindrome(s):
            return True

        length = len(s)

        for i in range(length / 2):
            j = length - i - 1
            if s[i] != s[j]:
                return self.isPalindrome(s[i + 1:j + 1]) or self.isPalindrome(s[i:j])
        return True

    def isPalindrome(self, s):
        length = len(s)
        left = 0
        right = length - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
