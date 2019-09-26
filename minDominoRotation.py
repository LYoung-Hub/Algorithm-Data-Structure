class Solution(object):

    def findRotation(self, A, B, aim):
        r_a = 0
        r_b = 0
        for a, b in zip(A, B):
            if a != aim and b != aim:
                return -1
            elif a != aim:
                r_a += 1
            elif b != aim:
                r_b += 1
        return min(r_a, r_b)

    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        d_a = self.findRotation(A, B, A[0])
        d_b = self.findRotation(B, A, B[0])
        if d_a != -1 and d_b != -1:
            return min(d_a, d_b)
        elif d_a == -1 or d_b == -1:
            return max(d_a, d_b)
        else:
            return -1
