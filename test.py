import sys
# in progress

def fun():
    n = int(raw_input())
    s = []
    for i in range(0, n):
        str = raw_input()
        s.append(str)

    re1 = True
    for i in range(0, n - 1):
        if len(s[i]) > len(s[i + 1]):
            re1 = False
            break

    re2 = True
    for i in range(0, n - 1):
        s1_len = len(s[i])
        for j in range(0, s1_len):
            if s[i][j] != s[i + 1][j] and ord(s[i][j]) > ord(s[i + 1][j]):
                re2 = False

    if re1 and not re2:
        print 'lexicographically'
    elif re2 and not re1:
        print 'lengths'
    elif re1 and re2:
        print 'both'


if __name__ == '__main__':
    fun()

