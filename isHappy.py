class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash_set = {}
        while n != 1:
            curr = n
            temp = 0
            while curr != 0:
                temp += pow(curr % 10, 2)
                curr /= 10
            n = temp
            if n in hash_set:
                return False
            else:
                hash_set[n] = True

        return True
