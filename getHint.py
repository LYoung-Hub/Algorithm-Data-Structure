class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt_a = 0
        cnt_b = 0

        hash_set_s = {}
        hash_set_g = {}
        for s, g in zip(secret, guess):
            if s == g:
                cnt_a += 1
            else:
                if s not in hash_set_s:
                    hash_set_s[s] = 1
                else:
                    hash_set_s[s] += 1
                if g not in hash_set_g:
                    hash_set_g[g] = 1
                else:
                    hash_set_g[g] += 1

        for hg in hash_set_g:
            while hash_set_g[hg] > 0:
                if hg in hash_set_s:
                    cnt_b += 1
                    hash_set_s[hg] -= 1
                    if hash_set_s[hg] == 0:
                        del hash_set_s[hg]
                hash_set_g[hg] -= 1

        return str(cnt_a) + 'A' + str(cnt_b) + 'B'


if __name__ == '__main__':
    solu = Solution()
    print solu.getHint('1122', '2211')
