class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        cnt_a = 0
        series_l = 0
        for e in s:
            if e == 'A':
                cnt_a += 1
            if cnt_a > 1:
                return False

            if e == 'L':
                series_l += 1
            else:
                series_l = 0

            if series_l > 2:
                return False

        return True
