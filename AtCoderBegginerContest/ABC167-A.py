s = input()
t = input()
lens = len(s)

if s == t[:lens] and s != t:
    print('Yes')
else:
    print('No')