class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curr = 0
        total = 0
        start = 0

        for i in range(0, len(gas)):
            curr += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1
