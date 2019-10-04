import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        else:
            primes = [True] * n
            primes[0], primes[1] = False, False
            for i in range(2, int(math.sqrt(n)) + 1):
                if primes[i]:
                    for j in range(i * i, n, i):
                        primes[j] = False
        return sum(primes)
