class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        length = len(s)
        ans = ''
        for i in range(0, length):
            left = i - 1
            right = i + 1
            temp = s[i]
            while left >= 0 and right < length and s[left] == s[right]:
                temp = s[left] + temp + s[right]
                left -= 1
                right += 1

            if len(ans) < len(temp):
                ans = temp

        for i in range(1, length):
            left = i - 1
            right = left + 1
            temp = ''
            while left >= 0 and right < length and s[left] == s[right]:
                temp = s[left] + temp + s[right]
                left -= 1
                right += 1

            if len(ans) < len(temp):
                ans = temp

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.longestPalindrome('babad')
