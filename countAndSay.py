class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dp = ['1', '11']
        if n == 1:
            return dp[0]

        if n == 2:
            return dp[1]

        for i in range(2, n):
            dp_str = dp[i - 1]
            j = 0
            count = 1
            result_str = ''
            while j < len(dp_str) - 1:
                if dp_str[j] == dp_str[j + 1]:
                    j += 1
                    count += 1
                else:
                    result_str = result_str + str(count) + dp_str[j]
                    count = 1
                    j += 1
            if dp_str[-1] == dp_str[-2]:
                result_str = result_str + str(count) + dp_str[-1]
            else:
                result_str = result_str + '1' + dp_str[-1]
            dp.append(result_str)

        return dp[-1]
