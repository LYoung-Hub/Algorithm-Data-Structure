class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= 1:
            return s

        zigzag = [''] * numRows
        zigzag[0] = zigzag[0] + s[0]
        step = 0
        dir = 1
        level = 0

        for i in range(1, len(s)):
            if step == numRows - 1:
                step = 0
                dir = -1 * dir

            if dir == 1:
                level += 1
            else:
                level -= 1

            zigzag[level] = zigzag[level] + s[i]

            step += 1

        ans = ''
        for i in range(0, len(zigzag)):
            ans = ans + zigzag[i]

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.convert('PAYPALISHIRING', 4)
