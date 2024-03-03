import sys
import itertools
x, y = map(int, input().split())

turtle = [i for i in range(x+1)]
crane = [i for i in range(x+1)]

for t, c in itertools.product(turtle, crane):
    if (4*t + 2*c == y) and (t + c == x):
        print('Yes')
        sys.exit()

print('No')