class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        mid = left + (right - left) / 2

        while left < right:
            if self.check(mid, weights, D):
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) / 2
        return right

    def check(self, load, weights, D):
        curr = 0
        done = 0
        all_w = sum(weights)
        for w in weights:
            if curr + w <= load:
                curr += w
            else:
                D -= 1
                curr = w
            if D == 0:
                break
            done += w
        if done == all_w:
            return True

        return False


if __name__ == '__main__':
    solu = Solution()
    print solu.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
