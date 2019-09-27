class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        length = len(path)
        if length == 0:
            return ''

        curr = ''
        idx = 0
        stack = []
        while idx < length:
            if path[idx] == '/':
                idx += 1
                if len(curr) > 0 and curr != '.' and curr != '..':
                    stack.append(curr)
                elif len(curr) > 0 and curr == '..' and stack:
                    stack.pop()
                curr = ''
                continue
            curr += path[idx]
            idx += 1

        if curr != '':
            if curr == '..' and stack:
                stack.pop()
            if curr != '.' and curr != '..':
                stack.append(curr)

        ans = ''
        if not stack:
            return '/'
        while stack:
            ans = '/' + stack.pop() + ans

        return ans


if __name__ == '__main__':
    solu = Solution()
    print solu.simplifyPath("/a//b////c/d//././/..")
