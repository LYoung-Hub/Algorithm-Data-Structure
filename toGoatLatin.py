class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        strs = S.split()
        alphabet = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i, s in enumerate(strs):
            if s[0] in alphabet:
                s += 'ma'
            else:
                s = s[1:] + s[0] + 'ma'
            s += 'a' * (i + 1)
        return ' '.join(strs)


if __name__ == '__main__':
    solu = Solution()
    print solu.toGoatLatin("I speak Goat Latin")
