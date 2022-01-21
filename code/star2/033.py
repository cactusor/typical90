import math

H, W = map(int, input().split())

if H == 1 or W == 1:
    ans = H * W  # 全てのLEDを点灯
    print(H*W)
else:
    # 奇数の行・列の場所の総数
    ans = math.ceil(H / 2) * math.ceil(W / 2)
    print(ans)