import sys
n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print(0)
    sys.exit()

else:
    multi = 1
    for i in a:
        multi *= i
        if multi > 10 ** 18:
            print(-1)
            sys.exit()

    print(multi)