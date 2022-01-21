# 8進数->10進数への変換
# 入力：string, 出力：int
def base8_to_10(S):
    ans = 0
    x = 1
    M = len(S)
    for i in range(M-1, -1, -1):
        ans += int(S[i]) * x
        x *= 8
    return ans

# 10進数->9進数への変換
# 入力：int, 出力：string
from collections import deque
def base10_to_9(T):
    ans = deque()
    if T == 0:
        return '0'
    while T > 0:
        ans.appendleft(str(T % 9))
        T //= 9
    return "".join(ans)

N, K = input().split()
K = int(K)

# 8進数->10進数->9進数->'8'を'5'に書き換え
for _ in range(K):
    base10 = base8_to_10(N)
    base9 = base10_to_9(base10)
    N = base9.replace('8', '5')

print(N)