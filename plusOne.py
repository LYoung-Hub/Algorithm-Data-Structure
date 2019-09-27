class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if length == 0:
            return []

        c = (digits[-1] + 1) / 10
        digits[-1] = (digits[-1] + 1) % 10
        if c == 0:
            return digits

        for i in range(length - 1, 0, -1):
            curr = (digits[i - 1] + c) % 10
            c = (digits[i - 1] + c) / 10
            digits[i - 1] = curr
            if c == 0:
                return digits

        return [c] + digits


if __name__ == '__main__':
    solu = Solution()
    print solu.plusOne([4, 9, 9, 9])
