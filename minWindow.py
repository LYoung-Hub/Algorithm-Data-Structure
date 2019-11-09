from collections import Counter, defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt_t = Counter(t)
        required_length = len(cnt_t)
        formed = 0
        curr_window = defaultdict(int)
        left, right = 0, 0
        ans = [float('inf'), 0, 0]
        while right < len(s):
            ch = s[right]
            curr_window[ch] += 1
            if ch in cnt_t and curr_window[ch] == cnt_t[ch]:
                formed += 1
            while left <= right and formed == required_length:
                tmp = s[left]

                if ans[0] > right - left + 1:
                    ans = [right - left + 1, left, right]

                curr_window[tmp] -= 1
                if tmp in cnt_t and curr_window[tmp] < cnt_t[tmp]:
                    formed -= 1
                left += 1
            right += 1
        return s[ans[1]: ans[2] + 1] if ans[0] < float('inf') else ''


if __name__ == '__main__':
    solu = Solution()
    print solu.minWindow("ADOBECODEBANC", "ABC")
