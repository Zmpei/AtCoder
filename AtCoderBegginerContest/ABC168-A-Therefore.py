N = input()
n = int(N[len(N)-1])  # N[-1]のほうが簡潔

if n == 3:
    print('bon')
elif n in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')

