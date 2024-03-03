n = int(input())
case = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for i in range(n):
    case[input()] += 1

for k, v in case.items():
    print('{} x {}'.format(k, v))
