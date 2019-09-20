class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0:
            return True

        if length % 2 != 0:
            return False

        stack = []

        for i in range(0, length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if not ((s[i] == ')' and top == '(') or (s[i] == ']' and top == '[') or (s[i] == '}' and top == '{')):
                    return False

        if len(stack) > 0:
            return False

        return True
