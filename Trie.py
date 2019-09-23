class Trie(object):

    hash_set = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if word not in self.hash_set:
            self.hash_set[word] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.hash_set

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        length = len(prefix)
        for ha in self.hash_set:
            if len(ha) >= length and ha[0:length] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
