class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        stack = []
        ans = ''
        for e in s:
            if e == ']':
                temp = ''
                while stack[-1] != '[':
                    top = stack.pop()
                    temp = top + temp
                stack.pop()
                num = ''
                while stack and len(stack[-1]) == 1 and ord('0') <= ord(stack[-1]) <= ord('9'):
                    num = stack.pop() + num
                if num != '':
                    num = int(num)
                    curr = 1
                    single = temp
                    while curr < num:
                        temp = temp + single
                        curr += 1
                stack.append(temp)
            else:
                stack.append(e)

        while stack:
            ans = stack.pop() + ans

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.decodeString("3[a]2[bc]")
