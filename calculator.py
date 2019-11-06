class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack, n, sign = [], 0, '+'
        for i in xrange(len(s)):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(n)
                elif sign == '-':
                    stack.append(-n)
                elif sign == '*':
                    stack.append(stack.pop() * n)
                else:
                    top = stack.pop()
                    if top // n < 0 and top % n != 0:
                        stack.append(top // n + 1)
                    else:
                        stack.append(top // n)
                sign = s[i]
                n = 0
        return sum(stack)


if __name__ == '__main__':
    solu = Solution()
    print solu.calculate('14-3/2')
