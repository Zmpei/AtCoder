n, k = map(int, input().split())
sunuke = list(range(1, n+1))  # すぬけ君n人
d = []  # inputを受け入れる配列（この後使ってない）

for i in range(k):
    d.append(int(input()))
    a_temp = (list(map(int, input().split())))
    for t in a_temp:
        if t in sunuke:
            sunuke.remove(t)

print(len(sunuke))
