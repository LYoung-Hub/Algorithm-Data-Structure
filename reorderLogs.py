class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        for s in logs:
            temp = s.split()
            if ord('a') <= ord(temp[-1][-1]) <= ord('z'):
                letter.append(s)
            else:
                digit.append(s)

        def f(l):
            temp = l.split(' ', 1)
            return temp[-1], temp[0]

        letter = sorted(letter, key=f)
        return letter + digit


if __name__ == '__main__':
    solu = Solution()
    print solu.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])
