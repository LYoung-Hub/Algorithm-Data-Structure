class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        r, g, b = costs[0]
        for i in range(1, len(costs)):
            curr_r, curr_g, curr_b = r, g, b
            r = min(curr_g, curr_b) + costs[i][0]
            g = min(curr_r, curr_b) + costs[i][1]
            b = min(curr_r, curr_g) + costs[i][2]
        return min(min(r, g), b)


if __name__ == '__main__':
    solu = Solution()
    print solu.minCost([[17,2,17],[16,16,5],[14,3,19]])
