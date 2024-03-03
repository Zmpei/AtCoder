import itertools

s = list(input())
ans = 'No'
combo = [0]*len(s)
last = list('02468')
for l in last:
    if l in s:
        combo[-1] = l
        s.remove(l)
        combo_s = list(itertools.permutations(s, r=len(s)))
        for c in combo_s:
            for i, j in enumerate(c):
                combo[i] = j
            a = int(''.join(combo))
            if a % 8 == 0:
                ans = 'Yes'
                break
            else:
                pass
    else:
        pass
    if ans == 'Yes':
        break
print(ans)