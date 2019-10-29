class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dic = [0] * 26
        for ch in licensePlate:
            if ord('A') <= ord(ch) <= ord('Z'):
                low_ch = ch.lower()
                dic[ord(low_ch) - ord('a')] += 1
            elif ord('a') <= ord(ch) <= ord('z'):
                dic[ord(ch) - ord('a')] += 1

        ans = ''
        min_len = float('inf')
        for w in words:
            temp = [0] * 26
            for ch in w:
                temp[ord(ch) - ord('a')] += 1
            if all(v1 >= v2 for v1, v2 in zip(temp, dic)) and len(w) < min_len:
                min_len = len(w)
                ans = w
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.shortestCompletingWord("GrC8950", ["measure","other","every","base","according","level","meeting","none","marriage","rest"])
