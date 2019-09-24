class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        else:
            ans = ''
            for s in strs:
                ans = ans + unichr(257) + s
            return ans

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return []
        else:
            strs = s.split(unichr(257))
            return strs[1:]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
