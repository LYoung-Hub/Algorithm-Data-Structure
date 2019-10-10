class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        return self.helper(coins, amount, [0] * amount)

    def helper(self, coins, remainder, cnt):
        if remainder < 0:
            return -1

        if remainder == 0:
            return 0

        if cnt[remainder - 1] != 0:
            return cnt[remainder - 1]

        curr_min = float('Inf')
        for c in coins:
            curr = self.helper(coins, remainder - c, cnt)
            if 0 <= curr < curr_min:
                curr_min = curr + 1
        cnt[remainder - 1] = curr_min if curr_min < float('Inf') else -1
        return cnt[remainder - 1]

