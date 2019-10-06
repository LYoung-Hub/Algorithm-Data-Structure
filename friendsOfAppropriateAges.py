class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageB <= 0.5 * ageA + 7 or ageB > ageA or (ageB > 100 and ageA < 100):
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA
        return ans
