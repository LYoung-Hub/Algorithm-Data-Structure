from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        word_length = len(beginWord)
        all_word_comb = defaultdict(list)
        for word in wordList:
            for i in range(0, word_length):
                all_word_comb[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque()
        q.append([(beginWord, 1)])
        visited = {beginWord: True}
        while q:
            curr, level = q.popleft()
            for i in range(0, word_length):
                comb = curr[:i] + '*' + curr[i + 1:]

                for w in all_word_comb[comb]:
                    if w == endWord:
                        return level + 1

                    if w not in visited:
                        q.append(w)
                        visited[w] = True

        return 0
