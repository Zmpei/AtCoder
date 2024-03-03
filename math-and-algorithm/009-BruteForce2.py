# bit全探索でTLEするほう
def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 'No'
    for i in range(2 ** N):
        total = 0
        for j in range(N):
            if i >> j & 1:
                total += A[j]
        if total == S:
            ans = 'Yes'
            break
    print(ans)


main()