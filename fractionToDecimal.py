class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        if remainder == 0:
            return sign + str(n)
        res = [sign + str(n), '.']
        stack = []
        while remainder != 0 and remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            res.append(str(n))

        if remainder != 0:
            idx = stack.index(remainder)
            res.insert(idx + 2, '(')
            res.append(')')

        return ''.join(res)
