class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length_one = len(num1)
        length_two = len(num2)

        ans = 0
        c = 0
        for i in range(0, length_one):
            one_sum = 0
            for j in range(0, length_two):
                re = (ord(num1[length_one - 1 - i]) - ord('0')) * (ord(num2[length_two - 1 - j]) - ord('0')) + c
                mul = re % 10
                c = re / 10
                one_sum += mul * pow(10, j)
            if c > 0:
                one_sum += c * pow(10, length_two)
                c = 0

            ans += one_sum * pow(10, i)

        return str(ans)


if __name__ == '__main__':
    solu = Solution()
    print solu.multiply('9', '9')
