from collections import Counter


class Solution(object):
    def perfectSubstring(self, s, k):
        ans = 0

        def helper(s, k):
            arr = Counter(s)
            return all(i == k for i in arr.values())

        left = 0
        right = left + k
        while right <= len(s):
            while right <= len(s):
                if helper(s[left: right], k):
                    ans += 1
                right += k
            left += 1
            right = left + k
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.perfectSubstring('1221221121', 3)
