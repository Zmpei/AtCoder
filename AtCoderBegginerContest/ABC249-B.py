S = input()
if len(S) == len(set(list(S))) and not S.isupper() and not S.islower():
    print('Yes')
else:
    print('No')
