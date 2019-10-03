import math


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        sign = {'+': True, '-': True, '*': True, '/': True}
        for i in tokens:
            if i not in sign:
                stack.append(int(i))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == '+':
                    stack.append(num2 + num1)
                elif i == '-':
                    stack.append(num2 - num1)
                elif i == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(math.trunc(num2 / float(num1)))

        return stack.pop()


if __name__ == '__main__':
    solu = Solution()
    print solu.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
