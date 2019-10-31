class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ans = [[r0, c0]]
        direction = True
        step = 1
        n = R * C
        while len(ans) < n:
            if direction:
                for c in xrange(step):
                    c0 += 1
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
                for r in xrange(step):
                    r0 += 1
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
            else:
                for c in xrange(step):
                    c0 -= 1
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
                for r in xrange(step):
                    r0 -= 1
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
            direction = not direction
            step += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.spiralMatrixIII(1,4,0,0)
