class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        encode_s = []
        for s in S:
            if len(encode_s) == 0:
                encode_s.append([s, 1])
            else:
                if s == encode_s[-1][0]:
                    encode_s[-1][1] += 1
                else:
                    encode_s.append([s, 1])

        ans = 0
        for word in words:
            encode_w = []
            curr = 0
            stretchy = True
            for chr in word:
                if len(encode_w) == 0:
                    if chr != encode_s[curr][0]:
                        stretchy = False
                        break
                    encode_w.append([chr, 1])
                else:
                    if chr == encode_w[-1][0]:
                        encode_w[-1][1] += 1
                    else:
                        if encode_s[curr][0] != encode_w[-1][0] or (encode_s[curr][0] == encode_w[-1][0] and ((
                                encode_w[-1][1] < encode_s[curr][1] < 3) or encode_w[-1][1] > encode_s[curr][1])):
                            stretchy = False
                            break
                        curr += 1
                        encode_w.append([chr, 1])
            if curr < len(encode_s) - 1 or encode_s[curr][0] != encode_w[-1][0] or (
                    encode_s[curr][0] == encode_w[-1][0] and ((encode_w[-1][1] < encode_s[curr][1] < 3) or
                                                              encode_w[-1][1] > encode_s[curr][1])):
                stretchy = False
            if stretchy:
                ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.expressiveWords("heeellooo", ["hello", "hi", "helo"])
