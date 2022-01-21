N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

ans = 0
for i in range(N):
    cnt = 0
    # 頂点iの隣接頂点の探索
    for gi in G[i]:
        if i > gi:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)