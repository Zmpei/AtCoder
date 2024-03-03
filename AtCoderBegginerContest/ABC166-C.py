n, m = map(int, input().split())
h = [int(_) for _ in input().split()]

elevation = {}
for _ in range(len(h)):
    elevation[_+1] = h[_]

obs = list([] for _ in range(len(h)))
for i in range(m):
    obsA, obsB = map(int, input().split())
    if elevation[obsA] == elevation[obsB]:  # elevation[obsA]のvalueをリストにしてTrue追加
        obs[obsA-1].append(0)  # 1==True, 0==False
        obs[obsB-1].append(0)
    elif elevation[obsA] > elevation[obsB]:
        obs[obsA-1].append(1)
        obs[obsB-1].append(0)
    elif elevation[obsA] < elevation[obsB]:
        obs[obsA-1].append(0)
        obs[obsB-1].append(1)

count = 0
for o in obs:  # obsの各リストでTrueの展望台の数をカウント
    if all(o):  # all()は空のリストでもTrueを返す
        count += 1

print(count)
# print(elevation)
# print(obs)