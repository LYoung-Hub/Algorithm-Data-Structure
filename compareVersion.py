class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        length_1 = len(version1)
        length_2 = len(version2)
        idx_1 = 0
        idx_2 = 0
        while idx_1 < length_1 and idx_2 < length_2:
            curr_1 = ''
            while idx_1 < length_1 and version1[idx_1] != '.':
                curr_1 += version1[idx_1]
                idx_1 += 1
            curr_1 = int(curr_1)

            curr_2 = ''
            while idx_2 < length_2 and version2[idx_2] != '.':
                curr_2 += version2[idx_2]
                idx_2 += 1
            curr_2 = int(curr_2)

            if curr_1 < curr_2:
                return -1
            elif curr_1 > curr_2:
                return 1

            idx_1 += 1
            idx_2 += 1

        while idx_1 < length_1:
            curr_1 = ''
            while idx_1 < length_1 and version1[idx_1] != '.':
                curr_1 += version1[idx_1]
                idx_1 += 1
            if curr_1 != '':
                curr_1 = int(curr_1)
                if curr_1 != 0:
                    return 1
            idx_1 += 1
        while idx_2 < length_2:
            curr_2 = ''
            while idx_2 < length_2 and version2[idx_2] != '.':
                curr_2 += version2[idx_2]
                idx_2 += 1
            if curr_2 != '':
                curr_2 = int(curr_2)
                if curr_2 != 0:
                    return -1
            idx_2 += 1

        return 0


if __name__ == '__main__':
    solu = Solution()
    print solu.compareVersion('1', '1.1')
