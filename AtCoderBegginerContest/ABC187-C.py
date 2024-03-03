import numpy as np

n = int(input())
s = np.array(list(input() for _ in range(n)))

condition = np.char.startswith(s, '!')
s_ = np.char.replace(s[condition], '!', '')

answer = 'satisfiable'
intersection = set(s) & set(s_)

if len(intersection) > 0:
    answer = intersection.pop()

print(answer)