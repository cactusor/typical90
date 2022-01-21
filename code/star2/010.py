N = int(input())

# 1組の累積和S、2組の累積和T
S = [0] * (N+1)
T = [0] * (N+1)
for i in range(N):
    ci, pi = map(int, input().split())
    if ci == 1:
        S[i+1] += pi
    else:
        T[i+1] += pi
    S[i+1] += S[i]
    T[i+1] += T[i]

# クエリごとに出力
Q = int(input())
for j in range(Q):
    lj, rj = map(int, input().split())
    sj = S[rj] - S[lj-1]
    tj = T[rj] - T[lj-1]
    print(sj, tj)