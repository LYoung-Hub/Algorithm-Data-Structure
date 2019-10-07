from collections import defaultdict


class DSU(object):

    def __init__(self):
        self.p = range(10001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(self.p[x])] = self.find(self.p[y])


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU()
        email_name = {}
        email_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_name[email] = name
                if email not in email_id:
                    email_id[email] = i
                    i += 1
                dsu.union(email_id[acc[1]], email_id[email])

        ans = defaultdict(list)
        for email in email_name:
            ans[dsu.find(email_id[email])].append(email)

        return [[email_name[v[0]]] + sorted(v) for v in ans.values()]
