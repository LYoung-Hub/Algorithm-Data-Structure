from collections import defaultdict


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        idx = 0
        length = len(paragraph)
        hash_set = defaultdict(int)
        while idx < length:
            curr = ''
            while idx < length and paragraph[idx] != ' ' and ord('a') <= ord(paragraph[idx]) <= ord('z'):
                curr += paragraph[idx]
                idx += 1
            if curr != '':
                hash_set[curr] += 1
            idx += 1

        for k in hash_set:
            if k in banned:
                hash_set[k] = 0

        max_curr = 0
        ans = ''
        for k in hash_set:
            if hash_set[k] > max_curr:
                max_curr = hash_set[k]
                ans = k
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
