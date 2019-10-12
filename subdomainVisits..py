from collections import Counter


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = Counter()
        for cp in cpdomains:
            cnt, domain = cp.split()
            cnt = int(cnt)
            s = domain.split('.')
            for i in range(0, len(s)):
                ans['.'.join(s[i:])] += cnt

        return ['{} {}'.format(c, d) for d, c in ans.items()]
