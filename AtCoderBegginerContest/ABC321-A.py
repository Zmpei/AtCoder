N, X = map(int, input().split())
A = list(map(int, input().split()))

# Nラウンド目のスコアを0から100まで試す
for score in range(101):
    A_with_score = A + [score]
    A_with_score.sort()
    sum_N = sum(A_with_score[1:-1])

    if sum_N >= X:
        print(score)
        break
else:
    print(-1)
