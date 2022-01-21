N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 配列Aを配列Bに置き換えるための操作回数
op = 0
for i in range(N):
    op += abs(A[i] - B[i])

# 操作回数がKより大きい場合は No
if op > K:
    print('No')
else:
    # パリティチェック(操作回数とKの偶奇が一致するか)
    if (op % 2 == 0 and K % 2 == 0) or (op % 2 == 1 and K % 2 == 1):
        print('Yes')
    else:
        print('No')