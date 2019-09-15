# -*- coding:utf-8 -*-
class Solution:
    def maxLengthOfSubstring(self, string, k):

        length = len(string)
        i = 0
        repeat_array = [1]
        char_array = [string[0]]
        while i < length - 1:
            if string[i] == string[i + 1]:
                repeat_array[-1] += 1
            else:
                char_array.append(string[i + 1])
                repeat_array.append(1)
            i += 1

        max_length = 0
        for i in range(0, len(repeat_array)):
            j = i
            dict = {}
            while j < len(char_array):
                if char_array[j] not in dict:
                    dict[char_array[j]] = 1
                if len(dict) == k:
                    break
                j += 1

            while j < len(char_array) and char_array[j] in dict:
                j += 1

            temp = sum(repeat_array[i:j])
            if temp > max_length:
                max_length = temp

        return max_length


if __name__ == '__main__':
    k = int(raw_input())
    string = raw_input()

    solu = Solution()
    print solu.maxLengthOfSubstring(string, k)

