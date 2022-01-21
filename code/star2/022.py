# 再帰処理回数を増やしておく
import sys
sys.setrecursionlimit(1000000)

# 自作のユークリッドの互除法.
def GCD(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return GCD(y, x % y)

#　入力
A, B, C = map(int, input().split())

# A, B, Cの最大公約数を求める
r = GCD(A, GCD(B, C))

ans = (A // r - 1) + (B // r - 1) + (C // r - 1)
print(ans)