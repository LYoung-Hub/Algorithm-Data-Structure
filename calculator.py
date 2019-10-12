class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_num = []
        stack_sign = []
        num = s
        num = num.replace('+', ' ')
        num = num.replace('-', ' ')
        num = num.replace('*', ' ')
        num = num.replace('/', ' ')
        nums = num.split()
        for n in nums:
            stack_num.append(int(n))

        for ch in s:
            if ch == '*' or ch == '/' or ch == '+' or ch == '-':
                stack_sign.append(ch)

        cnt = 0
        for i in range(0, len(stack_sign)):
            if stack_sign[i] == '*':
                stack_num[i + 1] = stack_num[i] * stack_num[i + 1]
                stack_num[i] = -1
                cnt += 1
            elif stack_sign[i] == '/':
                stack_num[i + 1] = stack_num[i] / stack_num[i + 1]
                stack_num[i] = -1
                cnt += 1

        for i in range(0, len(stack_sign)):
            if stack_sign[i] == '-':
                j = i
                while stack_num[j + 1] == -1:
                    j += 1
                stack_num[j + 1] *= -1
        return sum(stack_num) + cnt


if __name__ == '__main__':
    solu = Solution()
    print solu.calculate('14 - 3/2')
