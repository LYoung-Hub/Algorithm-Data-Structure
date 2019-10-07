class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_set = [0] * 26
        for t in tasks:
            tasks_set[ord(t) - ord('A')] += 1

        tasks_set = sorted(tasks_set)
        ans = 0
        while tasks_set[-1] > 0:
            curr = 0
            while curr <= n:
                if tasks_set[-1] == 0:
                    break
                if curr < 26 and tasks_set[25 - curr] > 0:
                    tasks_set[25 - curr] -= 1
                ans += 1
                curr += 1
            tasks_set = sorted(tasks_set)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
