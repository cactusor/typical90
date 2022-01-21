# 入力部分
H, W = map(int, input().split())
A = []
for _ in range(H):
    ai = list(map(int, input().split()))
    A.append(ai)

# i行の合計row[i]、j列目の合計col[j]を計算
row = [0] * H
col = [0] * W
for i in range(H):
    for j in range(W):
        row[i] += A[i][j]
        col[j] += A[i][j]

# 答えを計算して出力
for i in range(H):
    bi = []
    for j in range(W):
        bij = row[i] + col[j] - A[i][j]
        bi.append(bij)
    print(*bi)