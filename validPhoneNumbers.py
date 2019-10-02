def format(s):
    ans = ''
    for item in s:
        if 48 <= ord(item) <= 57:
            ans += '*'
        else:
            ans += item
    return ans


if __name__ == '__main__':
    dic = {'***-***-****': True, '(***) ***-****': True}

    f = open('file.txt')
    lines = f.readlines()
    ans = []
    for line in lines:
        format_line = format(line)
        if format_line in dic:
            ans.append(line)
    f.close()
    print ans

