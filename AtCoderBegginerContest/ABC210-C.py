def main():
    n, k = map(int, input().split())
    c = [int(_) for _ in input().split()]

    key = set(c)
    val = [0] * len(key)
    kv = dict(zip(key, val))

    ans = 0
    now = 0

    for i in range(n):
        if kv[c[i]] == 0:
            now += 1
        kv[c[i]] += 1

        if i >= k:
            kv[c[i-k]] -= 1
            if kv[c[i-k]] == 0:
                now -= 1

        ans = max(ans, now)
    return ans

if __name__ == '__main__':
    print(main())