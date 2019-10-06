class TrieNode(object):

    def __init__(self):
        self.cnt = 0
        self.children = [None] * 26
        self.end = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
                curr.cnt += 1
            curr = curr.children[idx]
        curr.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, idx, node):
        if len(word) == idx:
            return node.end

        ch = word[idx]
        if ch == '.':
            if node.cnt == 0:
                return False
            else:
                for n in node.children:
                    if n and self.searchHelper(word, idx + 1, n):
                        return True
                return False
        else:
            loc = ord(ch) - 97
            if not node.children[loc]:
                return False
            else:
                return self.searchHelper(word, idx + 1, node.children[loc])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    wordDict = WordDictionary()
    wordDict.addWord('a')
    wordDict.addWord('ab')
    wordDict.addWord('a')
    wordDict.search('a.')
    wordDict.search('ab')
    wordDict.search('.a')
    wordDict.search('.b')
    wordDict.search('ab.')
    wordDict.search('.')
    wordDict.search('..')
