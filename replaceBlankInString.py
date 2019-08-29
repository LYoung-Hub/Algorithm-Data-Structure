# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        strs = s.split(' ')
        ans = str(strs[0])
        for i in range(1, len(strs)):
            ans = ans + '%20' + str(strs[i])

        return ans


if __name__ == '__main__':
    solu = Solution()
    solu.replaceSpace('Hello world')
